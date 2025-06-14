from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1383470578341646436/QwVbnaqXoctkSyH6gUu85W_eT186Yzl-sU4cv1PQNXeLSEsVxgbg3WQh-fxkSVuAm1Ea"

@app.route('/')
def home():
    send_to_discord("say")
    return "Welcome! Discord has been notified."

def send_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print("Failed to send message:", response.text)

if __name__ == '__main__':
    app.run(debug=True)
