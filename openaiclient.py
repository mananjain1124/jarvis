


import openai
from config import apikey

openai.api_key = apikey

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a joke."}
        ]
    )
    print(response['choices'][0]['message']['content'])
except openai.error.RateLimitError:
    print("❌ Rate limit hit or no quota. Check billing or usage.")
except openai.error.AuthenticationError:
    print("❌ Invalid API key.")
except Exception as e:
    print("❌ Unexpected error:", str(e))



