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
import {ErrorPage} from "./components/errorPage";


const router = createBrowserRouter([
  {
    path: "/",
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
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
