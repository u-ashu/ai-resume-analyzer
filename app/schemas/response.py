from pydantic import BaseModel
from typing import Optional

class SkillMatch(BaseModel):
    percentage: float
    matched: list[str]
    missing: list[str]


class SemanticMatch(BaseModel):
    job_concept: str
    resume_concept: Optional[str] = None
    similarity: float
    confidence: str


class DynamicConcepts(BaseModel):
    resume: list[str]
    job_description: list[str]


class ResumeAnalysisResponse(BaseModel):
    filename: str
    overall_score: float
    skill_match: SkillMatch
    text_similarity: float
    dynamic_concepts: DynamicConcepts
    semantic_matches: list[SemanticMatch]
    recommendations: list[str]