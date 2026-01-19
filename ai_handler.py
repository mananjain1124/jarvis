# ai_handler.py
from groq import Groq
from config import groq_apikey
import datetime

# Initialize Groq
client = Groq(api_key=groq_apikey)

# Base system instruction
messages = [
    {"role": "system", "content": "You are Jarvis, a witty and helpful AI assistant. Keep answers concise."}
]

def get_response(user_query):
    global messages
    try:
        # Get current date/time dynamically
        now = datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
        
        # Add the new user message
        # We also inject the time so he knows it's "now"
        messages.append({"role": "user", "content": f"[{now}] {user_query}"})

        # --- THE FIX: MEMORY MANAGEMENT ---
        # If history is too long (more than 10 messages), cut it down.
        # We Keep index 0 (System Prompt) + the last 6 messages.
        if len(messages) > 10:
            messages = [messages[0]] + messages[-6:]

        # Call AI
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=250 # Limit answer size to save tokens
        )

        answer = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        
        return answer

    except Exception as e:
        # If we still hit a limit, clear memory completely and try one last time
        print(f"AI Error: {e}")
        messages = [messages[0]] # Reset memory
        return "My memory buffer was full. I have cleared it. Please ask again."
