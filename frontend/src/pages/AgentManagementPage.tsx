import React, { useState } from "react";
import AgentForm from "../components/agents/AgentForm";
import AgentListTable from "../components/agents/AgentListTable";
import AgentSimulator from "../components/agents/AgentSimulator";
const AgentManagementPage: React.FC = () => {
  const [refreshList, setRefreshList] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  return (
    <div className="p-6 space-y-6">
      <h2 className="text-xl font-bold">Agent Management</h2>
      <div className="flex gap-8">
        <div className="flex-1">
          <AgentForm onCreated={() => setRefreshList(r => r + 1)} />
        </div>
        <div className="flex-[2]">
          <AgentListTable key={refreshList} onSelect={setSelected} />
        </div>
      </div>
      {selected && (
        <div className="mt-8">
          <h3 className="font-bold mb-2">Simulate Conversation</h3>
          <AgentSimulator agentId={selected} />
        </div>
      )}
    </div>
  );
};
export default AgentManagementPage;