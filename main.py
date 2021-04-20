from typing import Optional

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

