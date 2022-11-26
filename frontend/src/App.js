import logo from './logo.svg';
import './App.css';
import {
  createBrowserRouter,
  RouterProvider,
  Route,
} from "react-router-dom";
import { EndPage } from "./pages/EndPage";
import { StartPage } from "./pages/StartPage";
import { TaskPage } from "./pages/TaskPage";
import { FailPage } from "./pages/FailPage";
import {ErrorPage} from "./components/errorPage";


const router = createBrowserRouter([
  {
    path: "/:eventId",
    element: <StartPage />,
    errorElement: <ErrorPage />
  },
  {
    path: '/task/:id',
    element: <TaskPage/>,
    errorElement: <ErrorPage />
  },
  {
    path: '/result/:id',
    element: <EndPage />,
    errorElement: <ErrorPage />
  },
  {
    path: '/fail',
    element: <FailPage />
  },
  {
    path: '*',
    element: <ErrorPage />
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
