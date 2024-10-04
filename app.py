# importing the librarires

import streamlit as st
import google.generativeai as genai
from langchain import PromptTemplate , LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# set up the local environment
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# designing the webpage
st.title("Movie Recommender System")
user_input = st.text_input("Enter the movie title,genre or keyword")


#create a propmt template

demo_template = '''think that you are frequent movie watcher who watches all films in\
    the world.you are a movie buff and movie lover . you know about all movies.\
        now if a movie name is given to you suggest movies similar genre to the movie which is
        mentioned.so now answer the following;{user_input}'''

template = PromptTemplate(
    input_variables = ['prompt'],
    template = demo_template
)

# initiate the model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("GOOGLE-API-KEY"))

if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f"Recommendations for you:\n {recommendations}")
else:
    st.write(" ")

