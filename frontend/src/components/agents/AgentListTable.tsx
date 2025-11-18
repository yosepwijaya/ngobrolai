import React, { useEffect, useState } from "react";

interface AgentItem {
  id: number;
  name: string;
  model: string;
}

const AgentListTable: React.FC<{ onSelect?: (id: number) => void }> = ({ onSelect }) => {
  const [agents, setAgents] = useState<AgentItem[]>([]);
  useEffect(() => {
    fetch("/agents/")
      .then(res => res.json())
      .then(setAgents);
  }, []);
  return (
    <table className="w-full border">
      <thead>
        <tr>
          <th className="text-left">Name</th>
          <th className="text-left">Model</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {agents.map(agent => (
          <tr key={agent.id}>
            <td>{agent.name}</td>
            <td>{agent.model}</td>
            <td>
              <button
                onClick={() => onSelect?.(agent.id)}
                className="text-blue-600 underline"
              >Select</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default AgentListTable;