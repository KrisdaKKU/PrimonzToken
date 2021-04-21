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
  return { "text":list_word }'''

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
  uvicorn.run(app, host="localhost", port=8080, debug=True)
