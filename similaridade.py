import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("merged_data.csv", encoding="ISO-8859-1", sep=",")

df = df.sample(n=10000)

df.dropna(inplace=True)

# Fill NA values
df['Location'].fillna('', inplace=True)
df['Book-Title'].fillna('', inplace=True)

# Combine location and book title into a single feature
df['Location_and_Book'] = df['Location'] + ' ' + df['Book-Title']

# Vectorize location and book title
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Location_and_Book'])

# Perform clustering
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# Assign labels to communities
df['Community'] = kmeans.labels_

df.to_csv('communities_by_similarity.csv', index=False)
