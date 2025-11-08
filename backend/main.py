"""Fast API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random


mood_to_tea = {
    "happy": ["Green Tea", "White Tea", "Jasmine Tea", "Sencha", "Rose Tea", "Chamomile"],
    "tired": ["Black Tea", "Matcha", "Yerba Mate", "Chai", "Pu-erh Tea", "Oolong Tea"],
    "stressed": ["Peppermint Tea", "Lemon Balm Tea", "Lavender Tea", "Chamomile", "Rooibos Tea"],
    "sad": ["Chamomile Tea", "Rooibos Tea", "Honey Ginger Tea", "Oolong Tea", "Hibiscus Tea"],
    "relaxed": ["Oolong Tea", "Chrysanthemum Tea", "Hibiscus Tea", "White Tea", "Mint Tea"],
    "focused": ["Matcha", "Pu-erh Tea", "Ginseng Tea", "Green Tea", "Black Tea"],
    "angry": ["Green Tea", "Ginger Tea", "Lemon Tea"],
    "anxious": ["Some tea", "Chamomile", "Lavender Tea", "Peppermint Tea"],
    "bored": ["Earl Grey", "Jasmine Tea", "Hibiscus Tea", "Chamomile Tea"],
    "excited": ["Sparkling Tea", "Fruit Infusion", "Sencha", "Matcha"],
    "confused": ["Mint Tea", "Chamomile Tea", "Oolong Tea"],
    "motivated": ["Yerba Mate", "Ginseng Tea", "Green Tea", "Black Tea"],
    "lonely": ["Rooibos Tea", "Chamomile", "Honey Ginger Tea", "Hibiscus Tea"]
}

encouragement_quotes = {
    "happy": [
        "Keep shining, your joy is contagious!",
        "Happiness looks good on you today!",
        "Our fate lives within us. You only have to be brave enough to see it.",
        "Happiness is the richest thing we will ever own.",
        "Joy is not in things; it is in us.",
        "Smiles are free, but their impact is priceless."
    ],
    "tired": [
        "Take a deep breath, you’ve got this!",
        "Rest if you need it — your mind will thank you.",
        "Even the strongest need to recharge.",
        "One step at a time, you’re doing enough."
    ],
    "stressed": [
        "This too shall pass. You are stronger than you think.",
        "Remember to take one step at a time.",
        "Focus on what you can control and let go of the rest.",
        "Stress is temporary; your resilience is permanent."
    ],
    "sad": [
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "You must not let anyone define your limits because of where you come from. Your only limit is your soul.",
        "All it takes is faith and trust.",
        "The things that make me different are the things that make me.",
        "When life gets you down, just keep swimming.",
        "Even on cloudy days, the sun is still shining above."
    ],
    "angry": [
        "If you do your best each and every day, good things are sure to come your way.",
        "The past can hurt. But you can learn and grow from it.",
        "Take a breath, calm your mind, then act with intention.",
        "Anger is temporary; wisdom lasts."
    ],
    "anxious": [
        "Even miracles take a little time.",
        "The flower that blooms in adversity is the most rare and beautiful of all.",
        "The very things that hold you down are going to lift you up.",
        "The only thing predictable about life is its unpredictability.",
        "Believe you can, then you will.",
        "No matter how the wind howls, the mountain cannot bow to it.",
        "Focus on the present moment; it’s your power."
    ],
    "bored": [
        "Creativity often comes from boredom — let it spark ideas!",
        "Try something new, even if it’s small.",
        "Every dull moment is an opportunity in disguise.",
        "Boredom is the canvas of innovation."
    ],
    "excited": [
        "Your energy is contagious — channel it wisely!",
        "Excitement is the spark that ignites greatness.",
        "Ride this wave of enthusiasm and create something amazing.",
        "Joy and excitement are signs that you’re on the right path."
    ],
    "confused": [
        "It’s okay to be unsure; clarity comes with time.",
        "Step back, breathe, and the path will reveal itself.",
        "Confusion is the first step toward understanding.",
        "Every question is a doorway to knowledge."
    ],
    "motivated": [
        "Keep pushing forward — your effort will pay off.",
        "Momentum comes from small consistent steps.",
        "Your determination today builds your success tomorrow.",
        "Believe in yourself and your journey."
    ],
    "relaxed": [
        "Enjoy the calm; it’s a gift to your mind and body.",
        "Peace begins with a deep breath.",
        "Relaxation is a form of self-respect.",
        "Take time to savor the present moment."
    ],
    "lonely": [
        "You are never truly alone; love starts within yourself.",
        "Reach out, connection is closer than you think.",
        "This moment of solitude is an opportunity to grow.",
        "Your presence is valuable, and so are you."
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




