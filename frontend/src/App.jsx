import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Home from "./components/Home";
import MainLayout from "./components/MainLayout";
import Login from "./components/Login";
import Register from "./components/Register";
import CreateTicket from "./components/CreateTicket";
import TicketList from "./components/TicketList";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <MainLayout />,
      children: [
        {
          path: "",
          element: <Home />,
        },
        {
          path: "login",
          element: <Login />,
        },
        {
          path: "register",
          element: <Register />,
        },
        {
          path: "create-ticket",
          element: <CreateTicket />,
        },
        {
          path: "ticket-list",
          element: <TicketList />,
        },
      ],
    },
  ]);

  return <RouterProvider router={router} />;
}

export default App;
