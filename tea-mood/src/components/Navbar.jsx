import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
import { useEffect, useState } from 'react'
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

function NavBar() {
    const [session, setSession] = useState(null);

    useEffect(() => {
    // Get current session
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session);
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange(
      (_event, session) => {
        setSession(session);
      }
    );


    return () => subscription.unsubscribe();
  }, []);


    const handleLogout = async () => {
        await supabase.auth.signOut()
    }
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/">
                        <h3>Home</h3>
                    </NavLink>
                    {!session && (
          <NavLink to="/Login"><h3>Sign In</h3></NavLink>
        )}
                     {session && (
          <NavLink onClick={handleLogout}>
            <h3>Log Out</h3>
          </NavLink>
        )}
                </NavMenu>
            </Nav>
        </>
    );
};


export default NavBar;
