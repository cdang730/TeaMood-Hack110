"""Fast API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from supabase import create_client, Client
import os
import random
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Connect to Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

mood_to_tea = {
    "happy": ["Green Tea", "White Tea", "Jasmine Tea"],
    "tired": ["Black Tea", "Matcha", "Yerba Mate"],
    "stressed": ["Peppermint Tea", "Lemon Balm Tea", "Lavender Tea"],
    "sad": ["Chamomile Tea", "Rooibos Tea", "Honey Ginger Tea"],
    "relaxed": ["Oolong Tea", "Chrysanthemum Tea", "Hibiscus Tea"],
    "focused": ["Matcha", "Pu-erh Tea", "Ginseng Tea"]
}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174",
                   "http://127.0.0.1:5174"],
    allow_credentials=False, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Example data model for POST requests
class MoodRequest(BaseModel):
    mood: str


@app.post("/mood/")
def get_tea(mood_request: MoodRequest):
    mood = mood_request.mood.lower()
    teas = mood_to_tea.get(mood)
    if teas: 
        recommended_tea = random.choice(teas)
    else:
        # if not return defalt tea
        recommended_tea = "Jasmine Tea"
    data = {"mood": mood, "recommended_tea": recommended_tea}
    response = supabase.table("moods").insert(data).execute()
    return {"mood": mood, "recommended_tea": recommended_tea, "message": f"For your {mood} mood, try {recommended_tea}!", "saved": bool(response.data)}




