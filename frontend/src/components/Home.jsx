import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="max-w-4xl mx-auto p-8">
      <h1 className="text-3xl font-semibold mb-4">
        Welcome to the Ticketing System
      </h1>
      <p className="mb-4">
        This is the home page of the ticketing system. Here you can view and
        manage your tickets.
      </p>
      <Link
        to="/create-ticket"
        className="bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700"
      >
        Create a New Ticket
      </Link>
    </div>
  );
}

export default Home;
