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
    "focused": ["Matcha", "Pu-erh Tea", "Ginseng Tea"], 
    "angry": ["Green Tea"],
    "anxious": ["Some tea"]
}

encouragement_quotes = {
    "happy": [
        "Keep shining, your joy is contagious!",
        "Happiness looks good on you today!", 
        "Our fate lives within us. You only have to be brave enough to see it.",
        "Happiness is the richest thing we will ever own."
    ],
    "tired": [
        "Take a deep breath, you’ve got this!",
        "Rest if you need it — your mind will thank you."
    ],
    "stressed": [
        "This too shall pass. You are stronger than you think.",
        "Remember to take one step at a time."
    ], 
    "sad": [
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "You must not let anyone define your limits because of where you come from. Your only limit is your soul.",
        "All it takes is faith and trust.", 
        "The things that make me different are the things that make me.", 
        "When life gets you down, do you wanna know what you've gotta do? Just keep swimming."
    ], 
    "angry": [
        "If you do your best each and every day, good things are sure to come your way.", 
        "The past can hurt. But from the way I see it, you can either run from it, or learn from it."
    ], 
    "anxious": [
        "Even miracles take a little time.", 
        "The flower that blooms in adversity is the most rare and beautiful of all.", 
        "The very things that hold you down are going to lift you up.", 
        "The only thing predictable about life is its unpredictability.",     "Believe you can, then you will.",
        "You see, when the world turns upside down, the best thing is to turn right along with it.", 
        "From failure, we learn, from success, not so much.", 
        "No matter how the wind howls, the mountain cannot bow to it."
    ]
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

class MoodRequest(BaseModel):
    mood: str


@app.post("/mood/")
def get_tea(mood_request: MoodRequest):
    mood = mood_request.mood.lower()
    teas = mood_to_tea.get(mood)
    quotes = encouragement_quotes.get(mood)
    
    if quotes:
        encouragement = random.choice(quotes) 
    else: 
        quotes = "Keep going, you’ve got this!"
    
    if teas: 
        recommended_tea = random.choice(teas)
    else:
        # if not return defalt tea
        recommended_tea = "Jasmine Tea"

    return {"mood": mood, 
            "recommended_tea": recommended_tea,
            "message": f"For your {mood} mood, try {recommended_tea}!",
            "encouragement": encouragement}




