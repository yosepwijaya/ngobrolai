import React from "react";

interface Props {
  sessionId: number;
  onBack?: () => void;
}

const ChatSessionDetail: React.FC<Props> = ({ sessionId, onBack }) => {
  // Demo data; replace with fetch by sessionId
  const messages = [
    { role: "user", text: "Hello" },
    { role: "agent", text: "Hi, how can I help you?" },
    { role: "user", text: "Show me the docs" },
    { role: "agent", text: "Here is what I found..." },
  ];
  return (
    <div className="bg-white border rounded p-4">
      <button className="mb-4 text-blue-600 underline" onClick={onBack}>&larr; Back</button>
      <h4 className="font-bold mb-2">Session #{sessionId}</h4>
      <div className="space-y-2 mb-2">
        {messages.map((m, i) => (
          <div key={i}>
            <span className="font-bold capitalize">{m.role}:</span> {m.text}
          </div>
        ))}
      </div>
    </div>
  );
};
export default ChatSessionDetail;