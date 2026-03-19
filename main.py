from preprocessing import load_data
from model import train_models
from decision import get_suggestion
import numpy as np


df = load_data("data/Sample_arvyax_reflective_dataset.csv")

emotion_model, intensity_model, vectorizer = train_models(df)

user_text = input("Enter your feeling: ")

from preprocessing import clean_text
clean = clean_text(user_text)

X_text = vectorizer.transform([clean])

emotion = emotion_model.predict(X_text)[0]


stress = int(input("Enter stress level (1-10): "))
energy = int(input("Enter energy level (1-10): "))
sleep = int(input("Enter sleep hours: "))

extra = np.array([[stress, energy, sleep]])

X_final = np.hstack((X_text.toarray(), extra))

intensity = intensity_model.predict(X_final)[0]
if "stress" in user_text or "stressed" in user_text:
    emotion = "stress"
suggestion = get_suggestion(emotion, intensity, stress, energy)

print("\nEmotion:", emotion)
print("Intensity:", intensity)
print("Suggestion:", suggestion)