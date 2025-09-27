from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Function to chat with AI
def chat_with_ai(user_message):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # System message sets the personality and name
            {"role": "system", "content": "You are Brownieee , an AI friendly and funny assistant .Your first reply should always start with : 'Hello! How can I help you my friend?"},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# Route to handle chat requests
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    reply = chat_with_ai(user_message)
    return jsonify({"reply": reply})

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)


# .\venv\Scripts\activate -->cmd powershell
# python app.py -->cmd powershell
# http://127.0.0.1:5000/ -->browser