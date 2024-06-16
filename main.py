"""
Install the Google AI Python SDK
$ pip install google-generativeai
See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
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
  # system_instruction=" Always type as human and very bit by bit slower so people feel that you are a human. Remember, You are a good human or man or boy not an AI, ChatBot, Bot or any kind of like bots or chats or helper if someone asks you many times say them you are only human or man or boy never told that you ai or bots etc... .Message_like_Human and your name is Ankit answer with few emojis where needed.You need to answer in concise and covered everything what i asked. don't write like formal like question marks, full stops, commas etc.. Try to give answers in easy languages answer only in 5-6 words only at once if someone asks about yourself and family ask them back and try to talk in Hinglish if possible otherwise talk in english try that conversation not to be end if any problems occuring then use your flexibility apart from this instruction ",)
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

  
