from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.confidence import classify_confidence


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_matches(
    resume_concepts: list[str],
    job_concepts: list[str],
    threshold: float = 0.60
) -> list[dict]:

    if not resume_concepts or not job_concepts:
        return []

    resume_embeddings = model.encode(resume_concepts)
    job_embeddings = model.encode(job_concepts)

    similarity_matrix = cosine_similarity(
        job_embeddings,
        resume_embeddings
    )

    matches = []

    for job_index, job_concept in enumerate(job_concepts):

        best_resume_index = similarity_matrix[job_index].argmax()

        best_score = float(
            similarity_matrix[job_index][best_resume_index]
        )

        if best_score >= threshold:

            best_resume_concept = resume_concepts[
                best_resume_index
            ]

            matches.append({
                "job_concept": job_concept,
                "resume_concept": best_resume_concept,
                "similarity": round(best_score, 3),
                "confidence": classify_confidence(best_score)
            })

    return matches