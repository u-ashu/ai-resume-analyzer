import { useEffect,useRef,useState } from "react";
import "./App.css";

function App() {
  const resultRef = useRef(null)
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  useEffect(()=>{
    if(result && resultRef.current){
      resultRef.current.scrollIntoView({
        behavior:"smooth",
        block:"start",
      })
    }
  },[result])

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume) {
      alert("Please upload your resume.");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Please enter the job description.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();

      formData.append("resume", resume);
      formData.append("job_description", jobDescription);

      const response = await fetch(
        "http://127.0.0.1:8000/analyze-resume",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "API request failed");
      }

      setResult(data);
      console.log("API RESPONSE:", data);

    } catch (error) {
      console.error("ERROR:", error);
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <div className="container">

        <h1>AI Resume Analyzer</h1>

        <p className="subtitle">
          Analyze your resume against a job description
        </p>

        <form onSubmit={handleSubmit}>

          <div className="form-group">

            <label>Upload Resume</label>

            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setResume(e.target.files[0])}
            />

          </div>

          <div className="form-group">

            <label>Job Description</label>

            <textarea
              placeholder="Paste the job description here..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />

          </div>

          <button type="submit" disabled={loading}>

            {loading ? "Analyzing..." : "Analyze Resume"}

          </button>

        </form>


        {result && (

          <div className="results" ref={resultRef}>

            <h2>Analysis Result</h2>


            {/* Overall Score */}

            <div className="score-card">

              <div className="score">
                {result.overall_score}%
              </div>

              <div className="score-label">
                Overall Resume Score
              </div>

            </div>


            {/* Skill Match */}

            <div className="skill-match-card">

              <div>

                <h3>Skill Match</h3>

                <p>
                  {result.skill_match.percentage}%
                </p>

              </div>

            </div>


            {/* Matched / Missing Skills */}

            <div className="skills-section">

              <div className="skills-card matched">

                <h3>✓ Matched Skills</h3>

                <div className="skill-list">

                  {result.skill_match.matched.map((skill) => (

                    <span
                      className="skill-badge"
                      key={skill}
                    >
                      {skill}
                    </span>

                  ))}

                </div>

              </div>


              <div className="skills-card missing">

                <h3>⚠ Missing Skills</h3>

                <div className="skill-list">

                  {result.skill_match.missing.length > 0 ? (

                    result.skill_match.missing.map((skill) => (

                      <span
                        className="skill-badge"
                        key={skill}
                      >
                        {skill}
                      </span>

                    ))

                  ) : (

                    <p className="no-missing">
                      No missing skills 🎉
                    </p>

                  )}

                </div>

              </div>

            </div>


            {/* Semantic Matches */}

            <div className="semantic-section">

              <h3>🧠 Semantic Matches</h3>

              {result.semantic_matches &&
              result.semantic_matches.length > 0 ? (

                <div className="semantic-list">

                  {result.semantic_matches.map(
                    (match, index) => (

                      <div
                        className="semantic-card"
                        key={index}
                      >

                        <div className="semantic-concepts">

                          <div>

                            <span className="semantic-label">
                              Job Requirement
                            </span>

                            <strong>
                              {match.job_concept}
                            </strong>

                          </div>


                          <span className="arrow">
                            →
                          </span>


                          <div>

                            <span className="semantic-label">
                              Resume Concept
                            </span>

                            <strong>
                              {match.resume_concept}
                            </strong>

                          </div>

                        </div>


                        <div className="semantic-info">

                          <span>
                            Similarity:{" "}
                            {(match.similarity * 100).toFixed(1)}%
                          </span>

                          <span>
                            Confidence:{" "}
                            {match.confidence}
                          </span>

                        </div>

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p>
                  No semantic matches found.
                </p>

              )}

            </div>


            {/* Recommendations */}

            <div className="recommendations-section">

              <h3>💡 Recommendations</h3>

              {result.recommendations &&
              result.recommendations.length > 0 ? (

                <div className="recommendations-list">

                  {result.recommendations.map(
                    (recommendation, index) => (

                      <div
                        className="recommendation-card"
                        key={index}
                      >
                        <span className="recommendation-icon">
                          →
                        </span>

                        <p>
                          {recommendation}
                        </p>

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p>
                  No recommendations at this time.
                </p>

              )}

            </div>


          </div>

        )}

      </div>

    </div>
  );
}

export default App;