import requests

API_KEY = "app-40tTGWRBojN35iUzQXkvXqnx"

url = "https://api.dify.ai/v1/chat-messages"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "inputs": {},
    "query": "インプレスのスッキリわかる入門シリーズってどんな本？",
    "response_mode": "blocking",
    "conversation_id": "",
    "user": "test-user"
}

response = requests.post(url, headers=headers, json=data)

result = response.json()
print(result["answer"])

"""
import openai

# APIキーの設定
openai.api_key = "xxxxxxxxxx"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
         "content":
         "インプレスのスッキリわかる入門シリーズって、どんな本？"}],
)
print(response.choices[0]["message"]["content"].strip())
"""