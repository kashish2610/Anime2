import streamlit as st
import pickle
import numpy as np
import pandas as pd
movies_df =pickle.load(open('Anime_list.pkl','rb'))
import gdown
url = "https://drive.google.com/uc?id=1VNnKhgB0xNdVq4qL6HbaWvAXIT0h1Gsb"
similarity= "similarity1.pkl"
gdown.download(url, similarity, quiet=False)
with open(similarity, "rb") as f:
    similarity_matrix = pickle.load(f)

movies_title= movies_df['name'].values
def recommend(movie):
    movie_index = movies_df[movies_df['name'] == movie].index[0]
    distance = similarity_matrix[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        movie_id=i[0]
        # fetch poster
        recommended_movies.append(movies_df.iloc[i[0]]['name'])
    return recommended_movies
st.title('Anime Recommender')
Selected_movie = st.selectbox(
"Select a Anime",
movies_title
)
if st.button("Recommend"):
    recommendations = recommend(Selected_movie)
    for i in recommendations:
        st.write(i)
