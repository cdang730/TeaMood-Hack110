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
    "mad": ["Hibiscus Tea","Rose Tea","Lavender Tea","Green Tea (lightly brewed)","Licorice Root Tea"],
    "anxious": ["Passionflower Tea","Ashwagandha Tea","Rooibos Tea","Oat Straw Tea"],
    "annoyed": ["Masala Chai", "Ceylon Tea", "Burdock Root Tea"],
    "excited": ["Dandelion Tea", "Earl Grey", "Kombucha Tea"],
    "goofy": ["Nettle Tea", "Valerian Root Tea", "Darjeeling Tea"],
    "confused": ["Turkish Tea", "Fenugreek Tea", "Assam Tea"]
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
        "Rest if you need it—your mind will thank you.",
        "The best weather comes after a storm."
    ],
    "stressed": [
        "This too shall pass. You are stronger than you think.",
        "Remember to take one step at a time."
    ], 
    "sad": [
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "You must not let anyone define your limits because of where you come from. Your only limit is your soul.",
        "All it takes is faith and trust.", 
        "The things that make me different are the things that make me me.", 
        "When life gets you down, do you wanna know what you've gotta do? Just keep swimming."
    ], 
    "mad": [
        "If you do your best each and every day, good things are sure to come your way.", 
        "The past can hurt. But from the way I see it, you can either run from it, or learn from it."
    ], 
    "anxious": [
        "Even miracles take a little time.", 
        "The flower that blooms in adversity is the most rare and beautiful of all.", 
        "The very things that hold you down are going to lift you up.", 
        "The only thing predictable about life is its unpredictability.",
        "Believe you can, then you will.",
        "You see, when the world turns upside down, the best thing is to turn right along with it.", 
        "From failure, we learn, from success, not so much.", 
        "No matter how the wind howls, the mountain cannot bow to it."
    ],
    "annoyed":[
        "All big waves will fade into tiny ripples.",
        "What irritates you is often no bigger than a bug.",
        "Some things are simply beyond your control; to escape, focus on what you can do."
    ],
    "excited":[
        "Great things lie ahead of you!",
        "The new day will dawn faster than you can blink.",
        "Everything will be even greater than you expected!"
    ],
    "goofy":[
        "Life is better with some humour!",
        "You're never too old to do goofy stuff.",
        "Instant gratification takes too long.",
        "Accept who you are, unless you're a serial killer."
    ],
    "confused":[
        "Follow your instincts and you will arrive to the right destination.",
        "There are many paths to take; don't feel pressured to always choose the right one.",
        "Sometimes, the best thing you can do when unsure is just ask!"
    ]
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174",
                   "http://127.0.0.1:5174",
                   "http://127.0.0.1:5173",
                   "http://localhost:5173"],
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
    
    if mood in mood_to_tea:
        encouragement = random.choice(quotes)
        recommended_tea = random.choice(teas)
        message = f"If you are {mood}, try {recommended_tea}!"
    else: 
        encouragement = "Keep going, you’ve got this!"
        recommended_tea = "Jasmine Tea"
        message = f"No matter how you feel, try {recommended_tea}!"

    return {"mood": mood, 
            "recommended_tea": recommended_tea,
            "message": message,
            "encouragement": encouragement}




