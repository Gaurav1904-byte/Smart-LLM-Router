from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Simple training dataset
X_train = [
    "What is 2+2?",
    "Define machine learning.",
    "Hello",
    "Explain gradient descent mathematically.",
    "Design scalable microservice architecture.",
    "Compare supervised and unsupervised learning in detail.",
    "Write a Python function to reverse a string.",
    "Derive backpropagation algorithm step by step."
]

# 0 = simple, 1 = complex
y_train = [0, 0, 0, 1, 1, 1, 0, 1]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X_train)

classifier = LogisticRegression()
classifier.fit(X_vec, y_train)


def estimate_complexity(query: str) -> float:
    vec = vectorizer.transform([query])
    prob = classifier.predict_proba(vec)[0][1]
    return float(prob)