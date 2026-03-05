import joblib
import re

class SarcasmClassifier:
    """Класс для обработки текста и предсказания сарказма."""
    
    def __init__(self, model_path: str, vectorizer_path: str):
        # Загружаем сохраненные файлы из Колаба
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def _preprocess(self, text: str) -> str:
        """Очистка текста."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def predict(self, text: str):
        """Метод для получения предсказания и вероятности."""
        clean_text = self._preprocess(text)
        vectorized_text = self.vectorizer.transform([clean_text])
        
        prediction = self.model.predict(vectorized_text)[0]
        # Берем максимальную вероятность из двух классов
        probability = self.model.predict_proba(vectorized_text).max()
        
        label = "Sarcasm" if prediction == 1 else "Not sarcasm"
        return {"class": label, "probability": round(float(probability), 2)}
