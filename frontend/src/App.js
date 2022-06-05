import './App.css';
import Home from './Home';
import 'bootstrap/dist/css/bootstrap.min.css';
import {ToastContainer} from "react-toastify"
import 'react-toastify/dist/ReactToastify.css'

function App() {
  return (
    <>
    <ToastContainer/>
    <Home/>
    </>
  );
}

export default App;
