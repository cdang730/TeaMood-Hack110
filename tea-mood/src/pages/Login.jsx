import { useEffect, useState } from 'react'
import { createClient } from '@supabase/supabase-js'

// HMR-safe singleton supabase client (keeps everything in this file)
const _supabase_url = import.meta.env.VITE_SUPABASE_URL
const _supabase_key = import.meta.env.VITE_SUPABASE_ANON_KEY
if (!_supabase_url || !_supabase_key) {
  console.warn('Missing Supabase env vars (VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY)')
}
if (!globalThis.__supabase_client__) {
  globalThis.__supabase_client__ = createClient(_supabase_url, _supabase_key)
}
const supabase = globalThis.__supabase_client__
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'
import { Navigate } from 'react-router-dom'

// Using shared `supabase` from `src/lib/supabaseClient`

export default function Login() {
  const [session, setSession] = useState(null)

  useEffect(() => {
    let isMounted = true
    supabase.auth.getSession().then(({ data: { session } }) => {
      if (isMounted) setSession(session)
    })

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      if (isMounted) setSession(session)
    })
    
    return () => {
      isMounted = false
      subscription.unsubscribe()
    }
  }, [])



  if (!session) {
    return (
      <div className="auth-wrapper" style={{ maxWidth: 420, margin: '2rem auto'}}>
        <Auth
          supabaseClient={supabase}
          appearance={{ theme: ThemeSupa }}
          // Hide all OAuth provider buttons, add more later if needed
          providers={[]}
        />
      </div>
    )
  }
  return <Navigate to="/" replace />
}