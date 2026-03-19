from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def train_models(df):
   vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=3000)
   X_text = vectorizer.fit_transform(df["clean_text"])
   y_emotion = df["emotional_state"]
   emotion_model = LogisticRegression(max_iter=500)
   emotion_model.fit(X_text, y_emotion)
   extra = df[["stress_level", "energy_level", "sleep_hours"]].values
   X_combined = np.hstack((X_text.toarray(), extra))
   y_intensity = df["intensity"]
   intensity_model = RandomForestClassifier()
   intensity_model.fit(X_combined, y_intensity)

   extra = df[["stress_level", "energy_level", "sleep_hours"]].values

   X_combined = np.hstack((X_text.toarray(), extra))

   return emotion_model, intensity_model, vectorizer