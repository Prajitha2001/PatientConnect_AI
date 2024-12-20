import os
from dotenv import load_dotenv
from groq import Groq

import requests
from flask import Flask, request, jsonify

from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

CORS(app)

client = Groq(
    api_key=os.environ.get("API_KEY"),
)


def get_reponse(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """You are a Doctor also give some advice to regular check up on health.
                Provide response in consistent manner around 50 words.
                """,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


@app.route("/", methods=["GET"])
def checkHealth():
    try:
        return jsonify({"status": "Health check ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        response = get_reponse(query)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


def get_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    return response.json()


@app.route("/test_users", methods=["GET"])
def test_users():
    try:
        response = get_users()
        users = response["data"]["data"]
        return jsonify(users)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
