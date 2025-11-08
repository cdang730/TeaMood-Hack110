import express from 'express'
import 'dotenv/config'              // if you installed dotenv
import { createClient } from '@supabase/supabase-js'

const app = express()
const port = process.env.PORT || 3000

// Create server/client using the service role key. This key bypasses RLS.
// Only use it on the server side in trusted code.
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY,
  { auth: { persistSession: false } } // keep server from storing session state
)

app.get('/api/profiles', async (req, res) => {
  // Example: fetch profiles table (service_role can bypass RLS — be careful)
  const { data, error } = await supabase.from('profiles').select('*')
  if (error) return res.status(500).json({ error })
  res.json({ data })
})

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`)
})