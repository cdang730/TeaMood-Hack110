import { useState } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import NavBar from './components/Navbar.jsx'
import Login from './pages/Login.jsx'

function Home() {

  return (
    <>
      <h1>Tea Mood</h1>
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
        <NavBarApp/>
    )
}
