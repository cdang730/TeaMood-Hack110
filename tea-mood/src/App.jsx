import { useState } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import NavBar from './components/Navbar.jsx'
import Login from './pages/Login.jsx'

function Home() {
  //Sets default mood and result
  const [mood, setMood] = useState('');
  const [tea, setTea] = useState("");
  const [result, setResult] = useState(null);
  
  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/mood/", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ mood }),
    })
    const data = await res.json();
    setResult(data);
  };

  return (
    <>
      <h1>Tea Mood</h1>
      <form onSubmit={handleSubmit}>
        <input type='text' value={mood} onChange={(e) => setMood(e.target.value)} placeholder='Enter your mood'/>
        <button type="submit">Get Tea</button>
      </form>
      {result && <h2>{result.message}</h2>}
    </>
  )
}


function NavBarApp(){
  return(
    <Router>
      <NavBar/>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/Login' element={<Login/>}/>
      </Routes>
    </Router>
  );
}
export default function MyApp(){
    return(
      <div>
        <NavBarApp/>
      </div>
    )
}
