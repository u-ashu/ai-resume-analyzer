def calculate_skill_score(
    job_requirements: list[str],
    exact_matches: list[str],
    semantic_matches: list[dict]
) -> float:

    if not job_requirements:
        return 0.0

    exact_set = set(exact_matches)

    total_score = 0.0

    for requirement in job_requirements:

        # Exact evidence
        if requirement in exact_set:
            total_score += 1.0
            continue

        # Semantic evidence
        best_similarity = 0.0

        for match in semantic_matches:

            if match["job_concept"] == requirement:

                best_similarity = max(
                    best_similarity,
                    match["similarity"]
                )

        total_score += best_similarity

    score = (
        total_score / len(job_requirements)
    ) * 100

    return round(score, 2)