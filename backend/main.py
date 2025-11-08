"""Fast API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

mood_to_tea = {
    "happy": ["Green Tea", "White Tea", "Jasmine Tea"],
    "tired": ["Black Tea", "Matcha", "Yerba Mate"],
    "stressed": ["Peppermint Tea", "Lemon Balm Tea", "Lavender Tea"],
    "sad": ["Chamomile Tea", "Rooibos Tea", "Honey Ginger Tea"],
    "relaxed": ["Oolong Tea", "Chrysanthemum Tea", "Hibiscus Tea"],
    "focused": ["Matcha", "Pu-erh Tea", "Ginseng Tea"]
}


app = FastAPI()

# Allow your frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] if using Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example data model for POST requests
class MoodRequest(BaseModel):
    mood: str

@app.get("/")
def read_root():
    return {"message": "Welcome to TeaMood FastAPI backend!"}

@app.post("/mood/")
def get_tea(mood_request: MoodRequest):
    mood = mood_request.mood.lower()
    teas = mood_to_tea.get(mood)
    if teas: 
        recommended_tea = random.choice(teas)
    else:
        # if not return defalt tea
        recommended_tea = "Jasmine Tea"
    return {"mood": mood, "recommended_tea": recommended_tea, "message": f"For your {mood} mood, try {recommended_tea}!"}



