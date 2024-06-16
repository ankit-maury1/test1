import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
generation_config = {
  "temperature": 0.3,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  system_instruction="You are an intelligent ai which can code everything and solve any problens in concise and easy language and beginer friendly")

history=[]
# user_input=""
print("Hello! ")
while True:
    user_input=input("You: ")
    chat_session = model.start_chat(history=history)
    
    try:
        if(user_input==""):
            x=input("Do you want to exit y/n?")
            if(x=='y'):
                exit()
        response = chat_session.send_message(user_input)
        model_response=response.text
        print(f"AI: {model_response}")
        history.append({"role": "model", "parts": [model_response]})
    except:
        print("Write here")
    history.append({"role": "user", "parts": [user_input]})

  
