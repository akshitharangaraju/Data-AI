import { useState } from "react";
import ChatUI from "./components/ChatUI";
import AgentDashboard from "./components/AgentDashboard";
import { askAgents } from "./api/api";

function buildAssistantMessage(result) {
  return {
    id: crypto.randomUUID(),
    role: "assistant",
    content: result.final_response,
  };
}

export default function App() {

  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState([]);
  const [dashboard, setDashboard] = useState(null);
  const [result, setResult] = useState(null);
  const [mode, setMode] = useState("graph");
  const [error, setError] = useState("");

  async function handleSubmit(event) {

    event.preventDefault();

    const nextPrompt = prompt.trim();

    if (!nextPrompt) return;

    const userMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: nextPrompt,
    };

    setMessages((current) => [...current, userMessage]);

    setPrompt("");
    setLoading(true);
    setError("");

    try {

      const response = await askAgents(nextPrompt, mode);

      setResult(response.result);
      setDashboard(response.result.dashboard);

      const assistantMessage = buildAssistantMessage(response.result);

      setMessages((current) => [...current, assistantMessage]);

    } catch (err) {

      setError("Something went wrong.");

    } finally {

      setLoading(false);

    }
  }

  return (

    <div className="mx-auto max-w-7xl space-y-6 p-6">

      <div className="flex gap-6">

        <div className="flex-1">

          {/* WORKFLOW SELECTOR */}

          <div className="mb-4 flex gap-6 text-white">

            <label>
              <input
                type="radio"
                value="graph"
                checked={mode === "graph"}
                onChange={(e) => setMode(e.target.value)}
              />
              Graph Workflow
            </label>

            <label>
              <input
                type="radio"
                value="crew"
                checked={mode === "crew"}
                onChange={(e) => setMode(e.target.value)}
              />
              Crew Workflow
            </label>

          </div>

          <ChatUI
            messages={messages}
            prompt={prompt}
            loading={loading}
            onPromptChange={(e) => setPrompt(e.target.value)}
            onSubmit={handleSubmit}
            result={result}
          />

        </div>

        <div className="w-[380px]">

          <AgentDashboard dashboard={dashboard} result={result} />

        </div>

      </div>

      {error && (
        <div className="text-red-400">{error}</div>
      )}

    </div>

  );
}