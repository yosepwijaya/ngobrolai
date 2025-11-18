import React, { useState } from "react";

interface AgentFormProps {
  onCreated?: () => void;
}

const AgentForm: React.FC<AgentFormProps> = ({ onCreated }) => {
  const [name, setName] = useState("");
  const [model, setModel] = useState("");
  const [creating, setCreating] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setCreating(true);
    await fetch("/agents/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, model }),
    });
    setCreating(false);
    setName("");
    setModel("");
    onCreated?.();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 border rounded">
      <div>
        <label className="block text-sm font-bold">Name</label>
        <input value={name} onChange={e => setName(e.target.value)} className="border rounded p-1 w-full" required />
      </div>
      <div>
        <label className="block text-sm font-bold">Model</label>
        <input value={model} onChange={e => setModel(e.target.value)} className="border rounded p-1 w-full" required />
      </div>
      <button type="submit" className="bg-blue-600 text-white px-4 py-1 rounded" disabled={creating}>
        {creating ? "Creating..." : "Create Agent"}
      </button>
    </form>
  );
};

export default AgentForm;