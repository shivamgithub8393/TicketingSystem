import { useState } from "react";

function TicketList() {
  const [tickets, setTickets] = useState([
    { id: 1, title: "Issue with login", status: "Open" },
    { id: 2, title: "Payment error", status: "Closed" },
    { id: 3, title: "Page not loading", status: "Open" },
  ]);
  return (
    <main className="container mx-auto py-6">
      <section>
        <h2 className="text-2xl font-semibold mb-4">Ticket List</h2>
        <div className="bg-white shadow-md rounded-lg p-6">
          <table className="w-full table-auto">
            <thead>
              <tr>
                <th className="px-4 py-2 text-left">Ticket Title</th>
                <th className="px-4 py-2 text-left">Status</th>
              </tr>
            </thead>
            <tbody>
              {tickets.map((ticket) => (
                <tr key={ticket.id} className="border-b">
                  <td className="px-4 py-2">{ticket.title}</td>
                  <td className="px-4 py-2">
                    <span
                      className={`px-3 py-1 text-sm font-semibold rounded-full ${
                        ticket.status === "Open"
                          ? "bg-yellow-500 text-white"
                          : "bg-green-500 text-white"
                      }`}
                    >
                      {ticket.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  );
}

export default TicketList;
