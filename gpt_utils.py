# gpt_utils.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_goal_details(goal: str):
    prompt = f"""
    Extract the following details from the goal:
    - Number of people
    - Cuisine
    - Location/area
    - City
    - Preferred time (if mentioned)

    Goal: {goal}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']