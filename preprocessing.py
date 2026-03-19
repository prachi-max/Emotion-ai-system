import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna()

    df["clean_text"] = df["journal_text"].apply(clean_text)

    return df