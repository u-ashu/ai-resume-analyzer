from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


TECHNICAL_REFERENCES = [
    # Programming
    "programming",
    "programming languages",
    "software development",
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "TypeScript",
    "SQL",

    # Backend
    "backend development",
    "server side development",
    "API development",
    "REST APIs",
    "web services",
    "FastAPI",
    "Django",
    "Flask",
    "Node.js",
    "Spring Boot",
    "RESTful APIs",
    "REST APIs",

    # Architecture
    "software architecture",
    "system architecture",
    "distributed systems",
    "distributed computing",
    "distributed architecture",
    "microservices",
    "microservices architecture",
    "event driven architecture",
    "event driven systems",
    "event driven applications",
    "service oriented architecture",

    # Databases
    "database systems",
    "database management",
    "relational databases",
    "SQL databases",
    "NoSQL databases",
    "MongoDB",
    "PostgreSQL",
    "MySQL",
    "Redis",

    # Cloud / DevOps
    "cloud computing",
    "cloud infrastructure",
    "AWS",
    "Azure",
    "Google Cloud",
    "containerization",
    "Docker",
    "Kubernetes",
    "DevOps",
    "CI/CD",
    "continuous integration",
    "continuous deployment",

    # Data / ML / AI
    "data engineering",
    "data science",
    "machine learning",
    "deep learning",
    "natural language processing",
    "artificial intelligence",
    "data analysis",

    # Distributed systems / messaging
    "message queues",
    "message brokers",
    "event streaming",
    "distributed messaging",
    "Apache Kafka",
    "Kafka",
    "RabbitMQ",
    "Amazon SQS",
    "Apache Spark",

    # Frontend
    "frontend development",
    "web development",
    "React",
    "React.js",
    "ReactJS",
    "Angular",
    "Vue.js",
]


REFERENCE_EMBEDDINGS = model.encode(TECHNICAL_REFERENCES)


def filter_technical_concepts(
    concepts: list[str],
    threshold: float = 0.40
) -> list[str]:

    if not concepts:
        return []

    concept_embeddings = model.encode(concepts)

    similarity_matrix = cosine_similarity(
        concept_embeddings,
        REFERENCE_EMBEDDINGS
    )

    technical_concepts = []

    for index, concept in enumerate(concepts):

        max_similarity = similarity_matrix[index].max()

        normalized_concept = concept.lower().strip()

        direct_match = any(
            normalized_concept == reference.lower()
            for reference in TECHNICAL_REFERENCES
        )

        print(
            f"CONCEPT: {concept:<30} "
            f"SIMILARITY: {max_similarity:.3f} "
            f"DIRECT: {direct_match}"
        )

        if direct_match or max_similarity >=0.85:
            technical_concepts.append(concept)
    return sorted(set(technical_concepts))