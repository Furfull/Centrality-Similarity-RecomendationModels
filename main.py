import pandas as pd

# Reading Users CSV
users_data = pd.read_csv('Asset\BX-Users.csv', sep=';', encoding='ISO-8859-1', na_values='NULL', on_bad_lines='skip')
users_df = pd.DataFrame(users_data)


# Reading Book Ratings CSV
book_ratings_data = pd.read_csv('Asset\BX-Book-Ratings.csv', sep=';', encoding='ISO-8859-1', on_bad_lines='skip')
book_ratings_df = pd.DataFrame(book_ratings_data)


# Reading Books CSV
books_data = pd.read_csv('Asset\BX-Books.csv', sep=';', encoding='ISO-8859-1', on_bad_lines='skip')
books_df = pd.DataFrame(books_data)


merged_user_ratings = pd.merge(users_df, book_ratings_df, on='User-ID', how='inner')

# Merge the result with Books on "ISBN"
merged_data = pd.merge(merged_user_ratings, books_df, on='ISBN', how='inner')

merged_data.to_csv('merged_data.csv', index=False)