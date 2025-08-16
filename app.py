import os
import gdown
import gzip
import pickle
import streamlit as st
import pandas as pd
import requests

# ---------------- Google Drive Download ----------------
FILE_ID = "1edTXk3NPMPwxDit4T3804VLBy635J-as"
DOWNLOAD_URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Download if not present
if not os.path.exists("similarity.pkl.gz"):
    print("Downloading compressed similarity file from Google Drive...")
    gdown.download(DOWNLOAD_URL, "similarity.pkl.gz", quiet=False)

# Load the compressed similarity matrix
with gzip.open("similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)

# ---------------- Load Movie Data ----------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# ---------------- Poster Fetch Function ----------------
@st.cache_data
def fetch_poster(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f0ed755798ab46008e2fb98adb398175&language=en-US"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        backdrop_path = data.get('backdrop_path')
        if backdrop_path:
            return "https://image.tmdb.org/t/p/w500/" + backdrop_path

        return "https://via.placeholder.com/500x750.png?text=No+Image"

    except Exception as e:
        print(f"Poster fetch error for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=No+Image"

# ---------------- Recommendation Function ----------------
def recommend(movie):
    movies_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# ---------------- Streamlit UI ----------------
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Pick a movie you want recommendations for:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
