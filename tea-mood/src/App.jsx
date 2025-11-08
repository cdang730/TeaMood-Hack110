import { useState, useEffect } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import NavBar from './components/Navbar.jsx'
import Login from './pages/Login.jsx'
import { createClient } from '@supabase/supabase-js'


// Create a single supabase client per browser context. This avoids the
// "Multiple GoTrueClient instances" warning during HMR without adding files.
const _supabase_url = import.meta.env.VITE_SUPABASE_URL
const _supabase_key = import.meta.env.VITE_SUPABASE_ANON_KEY
if (!_supabase_url || !_supabase_key) {
  console.warn('Missing Supabase env vars (VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY)')
}
if (!globalThis.__supabase_client__) {
  globalThis.__supabase_client__ = createClient(_supabase_url, _supabase_key)
}
const supabase = globalThis.__supabase_client__



function Home() {
  // Sets default mood and result
  const [mood, setMood] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/mood/", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ mood }),
    });
    const data = await res.json();
    setResult(data);
  };

  const [session, setSession] = useState(null);
      useEffect(() => {
      // Get current session
      supabase.auth.getSession().then(({ data: { session } }) => {
        setSession(session);
        if (!session){
          setResult(null);
        }
      });})

  return (
    <>
      <h1>Tea Mood</h1>
      {!session ? (
        <p>Please log in to get personalized tea suggestions.</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={mood}
            onChange={(e) => setMood(e.target.value)}
            placeholder="Enter your mood"
          /><br></br>
          <br></br>
          <button type="submit" className='submitButton'>Get Tea</button>
        </form>
      
      )
    }
    {result && <h2 className='tea-result'>{result.message}</h2>}
    {result && <h2 className='encouragement'>{result.encouragement}</h2>}
    </>
  );
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
