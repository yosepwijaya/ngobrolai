import React, { useState } from "react";

interface AgentSimulatorProps {
  agentId: number;
}

const AgentSimulator: React.FC<AgentSimulatorProps> = ({ agentId }) => {
  const [input, setInput] = useState("");
  const [responses, setResponses] = useState<string[]>([]);

  const handleSend = async () => {
    // Simulate API call; replace with real endpoint
    setResponses(r => [...r, "You: " + input, `Agent${agentId}: (simulated response)`]);
    setInput("");
  };

  return (
    <div className="border rounded p-4 space-y-2">
      <div className="h-32 overflow-y-auto bg-gray-50 border p-2 rounded">
        {responses.map((line, i) => (
          <div key={i}>{line}</div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          className="border rounded px-2 py-1 flex-1"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && handleSend()}
        />
        <button className="bg-blue-500 text-white px-3 py-1 rounded" onClick={handleSend} disabled={!input}>
          Send
        </button>
      </div>
    </div>
  );
};

export default AgentSimulator;