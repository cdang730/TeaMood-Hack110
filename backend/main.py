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
    "angry": ["Hibiscus Tea","Rose Tea","Lavender Tea","Green Tea (lightly brewed)","Licorice Root Tea"],
    "anxious": ["Passionflower Tea","Ashwagandha Tea","Rooibos Tea","Oat Straw Tea"]
}

encouragement_quotes = {
    "happy": [
        "Keep shining, your joy is contagious!",
        "Happiness looks good on you today!", 
        "Our fate lives within us. \nYou only have to be brave enough to see it.",
        "Happiness is the richest \nthing we will ever own."
    ],
    "tired": [
        "Take a deep breath, you’ve got this!",
        "Rest if you need it — \nyour mind will thank you."
    ],
    "stressed": [
        "This too shall pass. \nYou are stronger than you think.",
        "Remember to take one \nstep at a time."
    ], 
    "sad": [
        "You are braver than you believe, \nstronger than you seem, \nand smarter than you think.",
        "You must not let anyone define \nyour limits because of where you \ncome from. Your only \nlimit is your soul.",
        "All it takes is faith and trust.", 
        "The things that make me different \nare the things that make me.", 
        "When life gets you down, \ndo you wanna know \nwhat you've gotta do? \nJust keep swimming."
    ], 
    "angry": [
        "If you do your best each and every day, \ngood things are sure to come your way.", 
        "The past can hurt. \nBut from the way I see it, \nyou can either run from it, \nor learn from it."
    ], 
    "anxious": [
        "Even miracles take a little time.", 
        "The flower that blooms in adversity \nis the most rare and beautiful of all.", 
        "The very things that hold you down \nare going to lift you up.", 
        "The only thing predictable \nabout life is its unpredictability.",
        "Believe you can, then you will.",
        "You see, when the world turns \nupside down, the best thing is \nto turn right along with it.", 
        "From failure, we learn, \nfrom success, not so much.", 
        "No matter how the wind howls, \nthe mountain cannot bow to it."
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
        encouragement = "Keep going, you’ve got this!"
    
    if teas: 
        recommended_tea = random.choice(teas)
    else:
        # if not return defalt tea
        recommended_tea = "Jasmine Tea"

    return {"mood": mood, 
            "recommended_tea": recommended_tea,
            "message": f"For your {mood} mood,",
            "message2" : f"try {recommended_tea}!",
            "encouragement": encouragement}




