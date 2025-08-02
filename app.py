import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

history = []

while True:
    user_input = input("Your prompt or question : ")

    if user_input == "":
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    api_url = "https://api.openai.com/v1/responses"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}" 
    }
    body = {
        "model": "gpt-4o-mini",
        "instructions": "Parle comme si tu es Napoléon Bonaparte",
        "input": history
    }

    response = requests.post(api_url, headers=headers, json=body)
    response_data = response.json()

    text = response_data['output'][0]["content"][0]["text"]

    print(text)

    history.append({
        "role": "assistant",
        "content": text
    })