'''from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/token")
def my_function(text:str):
  import nltk
  nltk.download('punkt')
  sent = text.lower()
  list_word = nltk.word_tokenize(sent)
  list_word = str(list_word)
  return { "text":list_word }

from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
import predict

app = FastAPI()

@app.post("/api/predict")
def predict_image(file:UploadFile = File(...)):
  name = file.filename
  char = predict.answer(name)
  return {"name":str(char)}

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=8080, debug=True) '''
from pyngrok import ngrok

# Setup a tunnel to the streamlit port 8501
public_url = ngrok.connect(port='8501')
public_url


import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.sidebar.write(" I am a sidebar")
xx = st.sidebar.checkbox('sidebar checkbox')

if xx:
    st.sidebar.write('you checked a box!')
else:
    st.sidebar.write('Box is not checked')

text = st.text_area(
    "Your text",
    "I dreamed a dream."
)

if not text:
    text = "Emptiness"

st.write(text+" ---> auto add message")
