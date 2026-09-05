from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.response import ResumeAnalysisResponse

from app.services.pdf_extractor import extract_text_from_pdf
from app.services.text_processor import clean_text
from app.services.skill_extractor import extract_skills
from app.services.similarity import calculate_similarity
from app.services.scorer import calculate_skill_score
from app.services.recommendations import generate_recommendations
from app.services.dynamic_analyzer import extract_dynamic_concepts
from app.services.semantic_matcher import calculate_semantic_matches
from app.services.requirement_normalizer import normalize_requirements

from app.services.requirement_analyzer import build_requirements

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze a resume against a job description.",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post(
    "/analyze-resume",
    response_model=ResumeAnalysisResponse
)
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # --------------------------------
    # 1. Validate uploaded file
    # --------------------------------

    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported."
        )

    # --------------------------------
    # 2. Validate job description
    # --------------------------------

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    # --------------------------------
    # 3. Read uploaded PDF
    # --------------------------------

    resume_bytes = await resume.read()

    # --------------------------------
    # 4. Extract text from PDF
    # --------------------------------

    extracted_text = extract_text_from_pdf(resume_bytes)

    # --------------------------------
    # 5. Clean text
    # --------------------------------

    cleaned_resume = clean_text(extracted_text)
    cleaned_job_description = clean_text(job_description)

    # --------------------------------
    # 6. Extract exact skills
    # --------------------------------

    resume_skills = extract_skills(cleaned_resume)
    job_skills = extract_skills(cleaned_job_description)

    print("\nJOB DESCRIPTION:")
    print(repr(cleaned_job_description))

    print("\nJOB SKILLS:")
    print(job_skills)

    print("\nRESUME SKILLS:")
    print(resume_skills)

    # --------------------------------
    # 7. Extract dynamic concepts
    # --------------------------------

    resume_dynamic_concepts = extract_dynamic_concepts(
        cleaned_resume
    )

    job_dynamic_concepts = extract_dynamic_concepts(
        cleaned_job_description
    )

    print("\nRESUME DYNAMIC CONCEPTS:")
    print(resume_dynamic_concepts)

    print("\nJOB DYNAMIC CONCEPTS:")
    print(job_dynamic_concepts)

    # --------------------------------
    # 8. Normalize dynamic concepts
    # --------------------------------

    normalized_resume_concepts = normalize_requirements(
        resume_dynamic_concepts
    )

    normalized_job_concepts = normalize_requirements(
        job_dynamic_concepts
    )

    # Remove exact skills from dynamic concepts
    # Exact skills should only be matched using exact matching.
    job_skill_set = set(job_skills)
    resume_skill_set = set(resume_skills)

    normalized_job_concepts = [
        concept
        for concept in normalized_job_concepts
        if concept not in job_skill_set
    ]

    normalized_resume_concepts = [
        concept
        for concept in normalized_resume_concepts
        if concept not in resume_skill_set
    ]

    print("\nNORMALIZED RESUME CONCEPTS:")
    print(normalized_resume_concepts)

    print("\nNORMALIZED JOB CONCEPTS:")
    print(normalized_job_concepts)
    # Build unified job requirements
    job_requirements = build_requirements(
        job_skills,
        normalized_job_concepts
    )

    print("\nUNIFIED JOB REQUIREMENTS:")
    print(job_requirements)

    # --------------------------------
    # 9. Calculate semantic matches
    # --------------------------------

    # --------------------------------
# 9. Calculate semantic matches
# --------------------------------

    semantic_matches = calculate_semantic_matches(
        normalized_resume_concepts,
        normalized_job_concepts,
        threshold=0.60
    )

    print("\nSEMANTIC MATCHES:")
    print(semantic_matches)

    # --------------------------------
    # 10. Find exact matched skills
    # --------------------------------

    exact_matched_skills = (
        set(resume_skills) & set(job_requirements)
    )

    matched_skills = sorted(
        exact_matched_skills
    )

    # --------------------------------
    # 11. Find matched requirements
    # --------------------------------

    matched_requirements = set(
        matched_skills
    )

    # Add semantic matches
    for match in semantic_matches:

        matched_requirements.add(
            match["job_concept"]
        )

    matched_requirements = sorted(
        matched_requirements
    )

    # --------------------------------
    # 12. Find missing requirements
    # --------------------------------

    missing_requirements = sorted(
        set(job_requirements) - set(matched_requirements)
    )

    # --------------------------------
    # 13. Calculate requirement match %
    # --------------------------------

    if len(job_requirements) == 0:

        skill_match_percentage = 0.0

    else:

        skill_match_percentage = (
            len(matched_requirements)
            / len(job_requirements)
        ) * 100

    skill_match_percentage = round(
        skill_match_percentage,
        2
    )

    # --------------------------------
    # 14. Calculate text similarity
    # --------------------------------

    similarity_score = calculate_similarity(
        cleaned_resume,
        cleaned_job_description
    )

    # --------------------------------
    # 15. Calculate skill score
    # --------------------------------

    skill_score = calculate_skill_score(
        job_requirements,
        matched_skills,
        semantic_matches
    )

    # --------------------------------
    # 16. Calculate overall score
    # --------------------------------

    overall_score = round(
        (skill_score * 0.70)
        + (similarity_score * 100 * 0.30),
        2
    )

    # --------------------------------
    # 17. Generate recommendations
    # --------------------------------

    recommendations = generate_recommendations(
        missing_requirements,
        semantic_matches
    )

    # --------------------------------
    # 18. Return analysis
    # --------------------------------

    return {

        "filename": resume.filename,

        "overall_score": overall_score,

        "skill_match": {
            "percentage": skill_match_percentage,
            "matched": matched_requirements,
            "missing": missing_requirements
        },

        "text_similarity": round(
            similarity_score,
            2
        ),

        "dynamic_concepts": {
            "resume": resume_dynamic_concepts,
            "job_description": job_dynamic_concepts
        },

        "semantic_matches": semantic_matches,

        "recommendations": recommendations
    }