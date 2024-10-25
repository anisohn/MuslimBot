import requests
import json

def ask_question(question):
    url = "https://chatgpt-api8.p.rapidapi.com/"

    payload = [
        {
            "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
            "role": "system"
        },
        {
            "content": f"Je suis entrain de t'utiliser pour un bot discord qui répond uniquement aux questions concernant les religions et l'islam, donc réponds uniquement aux questions qui concernent ça, si la question ne concerne pas l'islam ou une religion, dis que tu ne réponds pas à ça, voilà la question : {question}",
            "role": "user"
        }
    ]
    headers = {
        "x-rapidapi-key": "c4e654c67bmshf3ac1e1c5161f08p12d395jsn156435ab76b4",
        "x-rapidapi-host": "chatgpt-api8.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    answer = data['text']   

    return answer
