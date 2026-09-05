from app.services.concept_extractor import extract_candidate_concepts
from app.services.concept_filter import filter_concepts
from app.services.semantic_filter import filter_technical_concepts


def extract_dynamic_concepts(text: str) -> list[str]:

    candidates = extract_candidate_concepts(text)

    print("\nCANDIDATES:")
    print(candidates)

    filtered_candidates = filter_concepts(candidates)

    print("\nAFTER GENERIC FILTER:")
    print(filtered_candidates)

    technical_concepts = filter_technical_concepts(
        filtered_candidates
    )

    print("\nAFTER TECHNICAL FILTER:")
    print(technical_concepts)

    return technical_concepts