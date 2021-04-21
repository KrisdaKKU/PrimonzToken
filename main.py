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

'''from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
import predict

app = FastAPI()

@app.post("/api/predict")
def predict_image(file:UploadFile = File(...)):
  #print('aaa')
  name = file.filename #.split('.')[-1] in ("jpg", "jpeg", "png","jfif")
  char = predict.answer(name)
  return str(char)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="localhost", port=2020, debug=True) '''
