#main.py

from fastapi import FastAPI
from pydantic import BaseModel
from gpt_utils import extract_goal_details
from places_api import search_restaurants
from calendar_utils import get_mock_availability
from automation import auto_book
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

class GoalRequest(BaseModel):
    goal: str

class BookingRequest(BaseModel):
    choice: int
    restaurant_name: str
    date: str
    time: str

@app.post("/goal")
def interpret_goal(data: GoalRequest):
    details = extract_goal_details(data.goal)
    return {"parsed_details": details}

@app.get("/restaurants")
def get_restaurants(location: str, cuisine: str):
    results = search_restaurants(location, cuisine)
    return {"restaurants": results}

@app.get("/availability")
def check_availability():
    return get_mock_availability()

@app.post("/confirm")
def confirm_booking(data: BookingRequest):
    auto_book(data.restaurant_name, data.date, data.time)
    return {
        "status": "Booking attempted for",
        "restaurant": data.restaurant_name
    }