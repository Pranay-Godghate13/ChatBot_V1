from dotenv import load_dotenv
load_dotenv()
import os

from langchain_groq import ChatGroq

def llm_chat_groq():


    llm=ChatGroq(
        #groq_api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.2
    )
    #chat_history=[{"role": "system", "content": "You are an AI assistant. Give answers precisely."}]
    while True:
        user_input=input("You: ")
        if(user_input=="exit"):
            break
        #chat_history.append({"role": "user", "content":user_input})
        chat_output=llm.invoke(chat_history)
        print("Assistant:",chat_output.content)
        #chat_history.append({"role": "assistant", "content":chat_output.content})
        
        
        
    
if __name__=="__main__":
    llm_chat_groq()