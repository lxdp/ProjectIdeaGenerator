import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import InitForm from "./components/InitialForm";
import ProjectIdeas from './components/ProjectIdeas';
import ProjectEvidence from './components/ProjectEvidence';
import SavedProject from './components/SavedProject';
import SavedProjectEvidence from './components/SavedProjectEvidence';
import RouteErrorBoundary from './components/RouteErrorBoundary';

const router = createBrowserRouter([
  {path: "/", element: <InitForm />, errorElement: <RouteErrorBoundary />},
  {path: "/project-ideas/:jobSearchId", element: <ProjectIdeas/>, errorElement: <RouteErrorBoundary />},
  {path: "/project-evidence/:uxInfoId", element: <ProjectEvidence/>, errorElement: <RouteErrorBoundary />},
  {path: "/saved-project/:id", element: <SavedProject/>, errorElement: <RouteErrorBoundary />},
  {path: "/saved-project-evidence/:requestedDataId", element: <SavedProjectEvidence/>, errorElement: <RouteErrorBoundary />}
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
