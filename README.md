# AI Resume Analyzer

An AI-powered full-stack application that analyzes a resume against a job description and identifies matched skills, missing requirements, semantic similarities, and personalized recommendations.

## 🚀 Features

* 📄 PDF resume upload and text extraction
* 🧠 NLP-based dynamic concept extraction
* 🔍 Exact technical skill matching
* 🤖 Transformer-based semantic matching using Sentence Transformers
* 📊 Resume-to-job skill match percentage
* 🎯 Overall resume compatibility score
* ⚠️ Identification of missing technical requirements
* 💡 Resume improvement recommendations
* ⚡ FastAPI backend
* ⚛️ React frontend
* 🔗 REST API integration between frontend and backend

## 🧠 How It Works

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Cleaning
    ↓
Exact Skill Extraction
    ↓
Dynamic NLP Concept Extraction
    ↓
Technical Concept Filtering
    ↓
Requirement Normalization
    ↓
Exact Matching + Semantic Matching
    ↓
Scoring
    ↓
Recommendations
    ↓
React Dashboard
```

## 🤖 AI / NLP

The project uses a hybrid approach:

### Exact Matching

Known technical skills are extracted from the resume and job description using normalized skill detection.

### Dynamic NLP Extraction

The system extracts technical concepts from the text using NLP rather than depending entirely on a predefined skills database.

### Semantic Matching

The project uses the `all-MiniLM-L6-v2` Sentence Transformer model to convert technical concepts into embeddings.

Cosine similarity is then used to determine how closely a resume concept matches a job requirement.

For example:

```text
Job Requirement       Resume Concept
-------------------------------------
distributed systems   distributed architecture
RESTful APIs          API development
microservices         microservices architecture
```

This allows the analyzer to identify related concepts even when the wording is different.

## 📊 Scoring

The analyzer combines multiple signals to calculate the overall resume score:

* Skill matching
* Semantic similarity
* Resume/job-description text similarity

The final score provides an overall indication of how closely the resume aligns with the provided job description.

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* spaCy
* Sentence Transformers
* scikit-learn

### Frontend

* React
* Vite
* CSS

### AI / NLP

* NLP-based concept extraction
* Sentence Transformers
* Cosine similarity
* Semantic matching

### Other

* Git
* GitHub
* REST API
* PDF text extraction

## 📁 Project Structure

```text
ai-resume-analyzer/
│
├── app/
│   ├── data/
│   │   └── skills.py
│   │
│   ├── services/
│   │   ├── concept_extractor.py
│   │   ├── concept_filter.py
│   │   ├── dynamic_analyzer.py
│   │   ├── pdf_extractor.py
│   │   ├── recommendation.py
│   │   ├── requirement_analyzer.py
│   │   ├── requirement_normalizer.py
│   │   ├── scorer.py
│   │   ├── semantic_filter.py
│   │   ├── semantic_matcher.py
│   │   ├── similarity.py
│   │   ├── skill_extractor.py
│   │   └── text_processor.py
│   │
│   ├── schemas/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/u-ashu/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

Make sure the required spaCy model is installed:

```bash
python -m spacy download en_core_web_sm
```

### 4. Start the backend

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 5. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

## 🔌 API

### Analyze Resume

```text
POST /analyze-resume
```

The endpoint accepts:

* `resume` — PDF resume
* `job_description` — job description text

Example response:

```json
{
  "filename": "resume.pdf",
  "overall_score": 72.45,
  "skill_match": {
    "percentage": 66.67,
    "matched": [
      "python",
      "fastapi",
      "sql"
    ],
    "missing": [
      "kafka",
      "docker"
    ]
  },
  "text_similarity": 0.68
}
```

## 🖥️ Application

The frontend provides a simple interface where users can:

1. Upload their resume
2. Paste a job description
3. Analyze the resume
4. View the overall score
5. See matched and missing requirements
6. Review semantic matches
7. Get recommendations for improving the resume

## 🔮 Future Improvements

* Resume section-level analysis
* Job description requirement prioritization
* Improved skill taxonomy
* Authentication and saved analyses
* Deployment to a cloud platform
* More advanced resume recommendations

## 👨‍💻 Author

**Ashutosh Tiwai**

GitHub: https://github.com/u-ashu
