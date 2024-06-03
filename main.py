import openai
import streamlit as st
import os
from lc_functions import split_text, initialize_llm, summarize_text

st.title("Audio to :blue[_Summary_]")

# Get the open AI API Key
api_key = st.text_input(
      label="OpenAI API Key", 
      placeholder="Ex: sk-2twmA8tfCb8un4...", 
      key="openai_api_key", 
      help="You can get your API key from https://platform.openai.com/account/api-keys/")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    openai.api_key = api_key

# File uploader
audio_file = st.file_uploader(label="Upload audio file", 
                         type=['wav','mp3','m4a'])


def transcribe_audio(audio_file):
    transcription = openai.Audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language='ko'
    )
    return transcription['text']


if audio_file is not None:
      # response = openai.Audio.transcribe(model="whisper-1", 
      #                                    file=audio, 
      #                                    api_key=api_key)
      # response = openai.audio.transcriptions.create(model="whisper-1", 
      #                                    file=audio_file,
      #                                    language='ko')
   # Split the text into chunks
  
      transcript = transcribe_audio(audio_file)
      # transcriptions = response["text"]
      docs = split_text(text=transcript, chunk_size=1000, chunk_overlap=100)
      #initialize the LLM
      llm = initialize_llm(model="gpt-4o", temperature=0.1, api_key=api_key)
      #llm2 = initialize_openai(model="gpt-3.5-turbo-16k", temperature=0, api_key=api_key)
      # create a summary
      summary = summarize_text(llm=llm, docs=docs)
      #summary2 = llm2(prompt_template_questions)
      st.write(summary)
