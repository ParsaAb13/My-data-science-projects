import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


file_path = "F:/python_project/IMDB Dataset.csv"
df = pd.read_csv(file_path)
print(df.head())

df["review"] = df["review"].str.lower().str.replace("<br />", " ", regex=False)


tfidf = TfidfVectorizer(max_features=1000)
X = tfidf.fit_transform(df["review"])


kmeans = KMeans(n_clusters=2, random_state=42)
df["cluster"] = kmeans.fit_predict(X)


print(df[["review", "sentiment", "cluster"]].head(10))


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())  

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, df['sentiment'], test_size=0.2)
model = LogisticRegression().fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test)}")

plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["cluster"], cmap='viridis', alpha=0.5)
plt.title("Clustering IMDB Reviews with TF-IDF & K-Means")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.colorbar(label='Cluster')
plt.show()