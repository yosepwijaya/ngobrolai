import React from "react";
import AgentManagementPage from "./pages/AgentManagementPage";
import ReportManagementPage from "./pages/ReportManagementPage";
const App = () => (
  <div className="container mx-auto p-6">
    <h1 className="text-2xl font-bold mb-6">Ngobrol.ai Dashboard</h1>
    <div className="mb-10"><AgentManagementPage /></div>
    <ReportManagementPage />
  </div>
);
export default App;