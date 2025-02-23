// src/lib/api.ts
const API_BASE_URL = "http://localhost:8000";

export async function makeApiRequest<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  console.log("Requesting:", `${API_BASE_URL}${endpoint}`); // Add this to debug
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error("Fetch error:", error);
    // Handle the error appropriately
    throw new Error();
  }
}
