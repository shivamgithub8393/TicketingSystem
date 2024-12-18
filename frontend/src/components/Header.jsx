import React from "react";
import { NavLink } from "react-router-dom";

const Header = () => {
  return (
    <header className="bg-blue-600 text-white py-4">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo */}
        <h1 className="text-3xl font-bold">
          <NavLink to="/" className="hover:text-gray-200">
            Ticketing System
          </NavLink>
        </h1>

        {/* Navigation Links */}
        <nav className="flex space-x-6">
          <NavLink
            to="/"
            className={({ isActive }) =>
              isActive
                ? "text-gray-900 bg-white py-2 px-4 rounded-md font-semibold transition-colors duration-200"
                : "text-white hover:text-gray-300 py-2 px-4 transition-colors duration-200"
            }
          >
            Home
          </NavLink>
          <NavLink
            to="/create-ticket"
            className={({ isActive }) =>
              isActive
                ? "text-gray-900 bg-white py-2 px-4 rounded-md font-semibold transition-colors duration-200"
                : "text-white hover:text-gray-300 py-2 px-4 transition-colors duration-200"
            }
          >
            Create Ticket
          </NavLink>
          <NavLink
            to="/ticket-list"
            className={({ isActive }) =>
              isActive
                ? "text-gray-900 bg-white py-2 px-4 rounded-md font-semibold transition-colors duration-200"
                : "text-white hover:text-gray-300 py-2 px-4 transition-colors duration-200"
            }
          >
            Ticket List
          </NavLink>
        </nav>
      </div>
    </header>
  );
};

export default Header;
