import React from "react";

interface ReportRequest {
  id: number;
  channel: string;
  status: string;
  created_at: string;
  file_url?: string;
}

const MOCK_REQUESTS: ReportRequest[] = [
  { id: 1, channel: "web", status: "Completed", created_at: "2023-06-01", file_url: "https://files.test/report1.xlsx" },
  { id: 2, channel: "api", status: "Pending", created_at: "2023-06-04" },
];

const ReportRequestTable: React.FC = () => (
  <table className="w-full border">
    <thead>
      <tr>
        <th>ID</th>
        <th>Channel</th>
        <th>Status</th>
        <th>Created</th>
        <th>File</th>
      </tr>
    </thead>
    <tbody>
      {MOCK_REQUESTS.map(r => (
        <tr key={r.id}>
          <td>{r.id}</td>
          <td>{r.channel}</td>
          <td>{r.status}</td>
          <td>{r.created_at}</td>
          <td>
            {r.file_url ? (
              <a className="text-blue-600 underline" href={r.file_url} target="_blank" rel="noopener noreferrer">Download</a>
            ) : "-"}
          </td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default ReportRequestTable;