import React from "react";

// Placeholder components
const AgentManagementPage = () => <div className="p-4 border rounded">Agent Management Module</div>;
const ReportManagementPage = () => <div className="p-4 border rounded mt-4">Report Management Module</div>;

const App = () => (
  <div className="container mx-auto p-6">
    <h1 className="text-2xl font-bold mb-6">Ngobrol.ai Dashboard</h1>
    <div className="mb-10"><AgentManagementPage /></div>
    <ReportManagementPage />
  </div>
);
export default App;
