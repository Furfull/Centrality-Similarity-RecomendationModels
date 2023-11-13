import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('communities_by_similarity.csv', delimiter=',', na_values='NULL')

df['Location'].fillna('', inplace=True)
df['Book-Title'].fillna('', inplace=True)

df['Location_and_Book'] = df['Location'] + ' ' + df['Book-Title']

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Location_and_Book'])

model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
model_knn.fit(tfidf_matrix)

def get_recommendations(title):
    if title not in df['Book-Title'].values:
        return "Book not found in the dataset."

    idx = df[df['Book-Title'] == title].index[0]

    distances, indices = model_knn.kneighbors(tfidf_matrix[idx], n_neighbors=11)

    book_indices = indices.squeeze().tolist()[1:]

    return df.loc[book_indices, 'Book-Title']


# Test the function with a book title from the dataset
print(get_recommendations("A Sand County Almanac (Outdoor Essays &amp; Reflections)"))


