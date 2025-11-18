import React, { useState } from "react";
import SessionHistoryTable from "../components/reports/SessionHistoryTable";
import ChatSessionDetail from "../components/reports/ChatSessionDetail";
import ReportRequestTable from "../components/reports/ReportRequestTable";
import ReportRequestForm from "../components/reports/ReportRequestForm";
const ReportManagementPage: React.FC = () => {
  const [activeSessionId, setActiveSessionId] = useState<number | null>(null);
  const [reportTableKey, setReportTableKey] = useState(0);
  const handleReportRequested = () => setReportTableKey(k => k + 1);
  return (
    <div className="p-6 space-y-6">
      <h2 className="text-xl font-bold">Conversation History</h2>
      {activeSessionId ? (
        <ChatSessionDetail sessionId={activeSessionId} onBack={() => setActiveSessionId(null)} />
      ) : (
        <SessionHistoryTable onSelect={setActiveSessionId} />
      )}
      <h2 className="text-xl font-bold mt-10">Report Management</h2>
      <div className="flex space-x-6">
        <div className="w-2/3"><ReportRequestTable key={reportTableKey} /></div>
        <div className="flex-1"><ReportRequestForm onRequest={handleReportRequested} /></div>
      </div>
    </div>
  );
};
export default ReportManagementPage;