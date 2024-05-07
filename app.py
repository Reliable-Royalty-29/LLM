#Conversational Q&A Chatbot
import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage

# Load environment variables from .env file
load_dotenv()

# # Define classes for different types of messages
# class SystemMessage:
#     def __init__(self, content):
#         self.content = content

# class HumanMessage:
#     def __init__(self, content):
#         self.content = content

# class AIMessage:
#     def __init__(self, content):
#         self.content = content

OPENAI_API_VERSION = "2024-02-01"
azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')

llm = AzureOpenAI(
    deployment_name="Dheeman",
    api_version=OPENAI_API_VERSION,
    azure_endpoint="https://d2912.openai.azure.com/",
    temperature=0.8
   
)

#Streamlit UI

# st.set_page_config(page_title="Conversational Q&A Chatbot")
# st.header("Hey, lets chat with AI")


if 'msg' not in st.session_state:
  st.session_state['msg']=[
    SystemMessage(content="Answer anything that huamna ask")
  ]

def test(question):
    st.session_state['msg'].append(HumanMessage(content=question))
    
    # Concatenate the content of messages into a single prompt string
    prompt = "\n".join(msg.content for msg in st.session_state['msg'])
    
    # Pass the concatenated prompt string to the language model
    answer = llm(prompt)
    
    st.session_state['msg'].append(AIMessage(content=answer))
    return answer


st.set_page_config(page_title="Q&A Demo")

st.header("Friendly Chatbot Application")

input=st.text_input("Ask your questions: ",key="input")
response=test(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
