import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

api_url = "https://api.openai.com/v1/responses"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}" 
}
body = {
    "model": "gpt-4o-mini",
    "input": "write a haiku about ai"
  }

response = requests.post(api_url, headers=headers, json=body)
response_data = response.json()

print(response_data)