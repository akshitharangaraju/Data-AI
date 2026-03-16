import axios from "axios";

const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function askAgents(query, mode) {

  const response = await client.post("/ask", {
    query: query,
    mode: mode
  });

  return response.data;
}