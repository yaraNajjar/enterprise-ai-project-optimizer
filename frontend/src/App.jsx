import { useState } from "react";
import { predictProject, getProjects } from "./api";

function App() {
  const [teamSize, setTeamSize] = useState("");
  const [issues, setIssues] = useState("");
  const [result, setResult] = useState(null);
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState(null); // ✅ new state

  const handlePredict = async () => {
    try {
      setError(null); // reset old error

      const res = await predictProject(
        Number(teamSize),
        Number(issues)
      );
      setResult(res);

      const allProjects = await getProjects();
      setProjects(allProjects);

    } catch (err) {
      console.error("Prediction error:", err);
      setError("Error: Prediction failed. Please try again."); // ✅ show UI error
    }
  };

  return (
    <div>
      <div style={{ marginBottom: '20px' }}>
        <label htmlFor="teamSize">Team Size:</label>
        <input
          id="teamSize"
          type="number"
          value={teamSize}
          onChange={(e) => setTeamSize(Number(e.target.value))}
        />
        <br />

        <label htmlFor="issues">Issues:</label>
        <input
          id="issues"
          type="number"
          value={issues}
          onChange={(e) => setIssues(Number(e.target.value))}
        />
        <br />

        <button style={{ marginTop: '10px' }} onClick={handlePredict}>
          Predict
        </button>
      </div>

      {/* ✅ error message shown in UI */}
      {error && (
        <p style={{ color: "red" }}>{error}</p>
      )}

      {result && (
        <div style={{ marginBottom: "20px" }}>
          <h2>Prediction Result</h2>
          <p>Duration: {result.predicted_duration}</p>
          <p>Cost: {result.predicted_cost}</p>
          <p>Delay Risk: {result.delay_risk ? "Yes" : "No"}</p>
        </div>
      )}

      {projects.length > 0 && (
        <div>
          <h2>Previous Projects</h2>
          <table border="1" cellPadding="5">
            <thead>
              <tr>
                <th>ID</th>
                <th>Team Size</th>
                <th>Issues</th>
                <th>Duration</th>
                <th>Cost</th>
                <th>Delay</th>
              </tr>
            </thead>
            <tbody>
              {projects.map(p => (
                <tr key={p.id}>
                  <td>{p.id}</td>
                  <td>{p.team_size}</td>
                  <td>{p.issues}</td>
                  <td>{p.predicted_duration}</td>
                  <td>{p.predicted_cost}</td>
                  <td>{p.delay_risk ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;
