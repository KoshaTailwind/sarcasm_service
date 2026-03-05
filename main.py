from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import SarcasmClassifier

# Создаем приложение
app = FastAPI(title="Sarcasm Detector API")

# Создаем объект класса
classifier = SarcasmClassifier('sarcasm_model.pkl', 'tfidf_vectorizer.pkl')

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Sarcasm Detection Service is Online!"}

@app.post("/predict")
def predict_sarcasm(request: TextRequest):
    # Вызываем метод из model_utils.py
    result = classifier.predict(request.text)
    return result
