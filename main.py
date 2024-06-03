import openai
import streamlit as st
import os
from lc_functions import split_text, initialize_llm, summarize_text

st.title("Audio to :blue[_Summary_]")

st.text("use the OpenAI Whisper function to convert your audio recording to a summary")
st.text("use gpt-3.5-turbo-16k: faster and significantly cheaper to run")
st.text('coded by Dr. Tseng  @zinojeng')


# Get the open AI API Key
api_key = st.text_input(
      label="OpenAI API Key", 
      placeholder="Ex: sk-2twmA8tfCb8un4...", 
      key="openai_api_key", 
      help="You can get your API key from https://platform.openai.com/account/api-keys/")
os.environ["OPENAI_API_KEY"] = api_key

# File uploader
audio = st.file_uploader(label="Upload audio file", 
                         type=['wav','mp3','m4a'])
if audio is not None:
      # response = openai.Audio.transcribe(model="whisper-1", 
      #                                    file=audio, 
      #                                    api_key=api_key)
      response = openai.audio.transcriptions.create(model="whisper-1", 
                                         file=audio)
   # Split the text into chunks
   
      transcript = response["text"]
      docs = split_text(text=transcript, chunk_size=1000, chunk_overlap=100)
      #initialize the LLM
      llm = initialize_llm(model="gpt-3.5-turbo-16k", temperature=0.1, api_key=api_key)
      #llm2 = initialize_openai(model="gpt-3.5-turbo-16k", temperature=0, api_key=api_key)
      # create a summary
      summary = summarize_text(llm=llm, docs=docs)
      #summary2 = llm2(prompt_template_questions)
      st.write(summary)
