from fastapi import FastAPI,File,UploadFile
from utils.exctract import extract_text_from_pdf
from utils.preprocessing import clean_text
from utils.matcher import calculate_similarity
from utils.skills_extractor import extract_skills
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer Backend Running 🚀"}


@app.post("/uplaod-resume")
async def upload_resume(file:UploadFile = File(...)):
    content = await file.read()
    extracted_text = extract_text_from_pdf(content)
    cleaned_text = clean_text(extracted_text)
    
    
    job_description = """
    We are looking for a Python developer with experience in Django,
    FastAPI, machine learning, pandas, numpy and scikit-learn.
    """
    
    resume_skills = extract_skills(cleaned_text)
    job_skills = extract_skills(job_description)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    if len(job_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(job_skills)) * 100
    
    similarity = calculate_similarity(cleaned_text, job_description)
    
    
    return{
        "filename":file.filename,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }
    
    