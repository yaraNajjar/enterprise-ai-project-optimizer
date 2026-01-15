const API_URL = "http://localhost:8080"; // Spring backend

// Predict using path variables (GET)
export async function predictProject(teamSize, issues) {
  const response = await fetch(
    `${API_URL}/predict/${teamSize}/${issues}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch prediction");
  }

  return response.json();
}

// Get all projects
export async function getProjects() {
  const response = await fetch(`${API_URL}/projects`);

  if (!response.ok) {
    throw new Error("Failed to fetch projects");
  }

  return response.json();
}
