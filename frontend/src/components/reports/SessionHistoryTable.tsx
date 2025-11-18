import React from "react";

interface Props {
  onSelect?: (id: number) => void;
}

const SessionHistoryTable: React.FC<Props> = ({ onSelect }) => {
  // Hardcoded demo data; replace with real fetch
  const sessions = [
    { id: 1, agent: "Agent Alpha", started_at: "2023-05-01", tokens_in: 10, tokens_out: 40 },
    { id: 2, agent: "Agent Beta", started_at: "2023-05-04", tokens_in: 20, tokens_out: 70 },
  ];
  return (
    <table className="w-full border">
      <thead>
        <tr>
          <th>Session ID</th>
          <th>Agent</th>
          <th>Start</th>
          <th>Input</th>
          <th>Output</th>
          <th>Detail</th>
        </tr>
      </thead>
      <tbody>
        {sessions.map(s => (
          <tr key={s.id}>
            <td>{s.id}</td>
            <td>{s.agent}</td>
            <td>{s.started_at}</td>
            <td>{s.tokens_in}</td>
            <td>{s.tokens_out}</td>
            <td>
              <button
                className="text-blue-600 underline"
                onClick={() => onSelect?.(s.id)}
              >Detail</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
export default SessionHistoryTable;