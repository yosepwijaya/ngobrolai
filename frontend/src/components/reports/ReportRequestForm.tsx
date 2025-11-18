import React, { useState } from "react";

interface Props {
  onRequest?: () => void;
}

const ReportRequestForm: React.FC<Props> = ({ onRequest }) => {
  const [channel, setChannel] = useState("");
  const [sending, setSending] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSending(true);
    // Simulate request here; replace with POST
    setTimeout(() => {
      setSending(false);
      setChannel("");
      onRequest?.();
    }, 1000);
  };

  return (
    <form className="space-y-2 border rounded p-4" onSubmit={handleSubmit}>
      <div>
        <label className="block text-sm">Channel</label>
        <input className="border rounded px-2 py-1 w-full" value={channel} onChange={e => setChannel(e.target.value)} required />
      </div>
      <button type="submit" className="bg-green-600 text-white px-4 rounded" disabled={sending}>
        {sending ? "Requesting..." : "Request Report"}
      </button>
    </form>
  );
};

export default ReportRequestForm;