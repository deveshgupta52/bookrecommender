import pickle
import streamlit as st
import numpy as np
import random

st.header("Book Recommender System using Machine Learning")

model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []
    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)
    for ids in ids_index:
        url = final_rating.iloc[ids]['img_url']
        poster_url.append(url)
    return poster_url

def recommend_books(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=15)
    suggestions = suggestions.flatten()
    random_suggestions = random.sample(list(suggestions), min(5, len(suggestions)))
    poster_url = fetch_poster([random_suggestions])
    recommended_books = [book_pivot.index[i] for i in random_suggestions]
    return recommended_books, poster_url        

selected_books = st.selectbox("Select a book", books_name)

if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)
    cols = st.columns(len(recommendation_books))
    for i, col in enumerate(cols):
        with col:
            st.text(recommendation_books[i])
            st.image(poster_url[i] if i < len(poster_url) else "https://via.placeholder.com/150")
