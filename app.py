import streamlit as st
import pandas as pd
import pickle
import requests
import os
from dotenv import load_dotenv
import base64

# Set page configuration at the top
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# Load environment variables
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# Load data
movies_dict = pickle.load(open('movie_dict (1).pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity (1).pkl', 'rb'))

# Function to encode image to base64
def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set background using base64 image
def set_background(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    background_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set background with your uploaded image
set_background("background.jpg")  

# Fetch poster from TMDb
def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/150x220.png?text=No+Poster"

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_titles, recommended_posters

# Streamlit UI
st.markdown("""
    <div style='text-align: center; background-color: rgba(0,0,0,0.2); padding: 10px; border-radius: 10px;'> <!-- Reduced opacity to 0.2 -->
        <h1 style='color:#FF4B4B;'>🎬 Movie Recommendation System 🍿</h1>
        <h4 style='color:white;'>Your go-to app for personalized movie suggestions!</h4>
        <p style='color:white;'>Pick a movie below and get 🔝 5 similar movies instantly — with posters!</p>
    </div>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox("👇 Pick a movie you like:", movies['title'].values)

if st.button("🚀 Recommend Movies"):
    with st.spinner("🔍 Fetching your recommendations..."):
        titles, posters = recommend(selected_movie_name)

    st.success("✅ Here are 5 movies you might enjoy:")

    cols = st.columns(5)
    for col, title, poster in zip(cols, titles, posters):
        with col:
            st.image(poster, caption=title, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: lightgray;'>✨ Built with ❤️ and ☕ by Oluwabukolami Arigbede using Streamlit</p>", unsafe_allow_html=True)
