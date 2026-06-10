import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN=os.getenv("HF_API_TOKEN")

if not HF_API_TOKEN:
    raise ValueError("HF_API_TOKEN environment variable is not set")

API_URL="https://router.huggingface.co/hf-inference/models/BAAI/bge-large-en-v1.5/pipeline/feature-extraction"
headers={
    "Authorization":f"Bearer {os.environ['HF_API_TOKEN']}",
}

def query(payload):
    response=requests.post(API_URL,headers=headers,json=payload)
    return response.json()

output=query({
    "inputs":"Today is a sunny day and I will get some ice cream.",
})

print(len(output))
print(output[:20])