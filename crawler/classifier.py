import pandas as pd
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('E:\\FakeNewsClassifier\\dataset.csv')
df.columns