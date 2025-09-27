import os
import openai
import pyttsx3
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chat_with_ai(prompt):
    # New OpenAI API usage
    response = openai.chat.completions.create(
        model="gpt-4o-mini",   # or "gpt-4.1" if your account supports
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🤖 AI Assistant Ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Assistant: Goodbye! 👋")
            speak("Goodbye!")
            break

        reply = chat_with_ai(user_input)
        print("Assistant:", reply)
        speak(reply)

#.\venv\Scripts\activate
# python main.py

