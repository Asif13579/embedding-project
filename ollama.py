import requests

url="http://localhost:11434/api/embeddings"
payload={
    "model":"nomic-embed-text",
    "prompt":"The sky is blue because of Rayleigh scattering"
}

response=requests.post(url,json=payload)
print(response.json())
print(len(response.json()['embedding']))