# Content Based Movie-Recommendation-System
📌 Overview
This project is a content-based movie recommender system that suggests movies similar to a given movie based on its metadata. The system utilizes Natural Language Processing (NLP) techniques to analyze movie features such as genres, keywords, cast, and crew and then recommends similar movies using cosine similarity.

Content-based filtering relies on the idea that if a user likes a particular movie, they will likely enjoy similar movies based on shared characteristics. This method does not require user interaction data, making it useful when user preferences are not available.

📊 Dataset
The dataset used in this project comes from The Movie Database (TMDB) Metadata available on Kaggle:
[🔗 TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The following two files are used for building the recommendation system:

movies.csv – Contains metadata such as movie title, genres, overview, and keywords.
credits.csv – Provides information about the cast and crew of each movie.

🏗️ Approach
1️⃣ Data Preprocessing
Extract important features: Title, Genres, Keywords, Cast, Crew.
Convert multiple genres and keywords into a single combined string for each movie.
Process text data by removing stopwords, punctuation, and special characters.
Convert text to lowercase and apply stemming (reducing words to their root form).
2️⃣ Feature Engineering
Convert processed text into numerical feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency) or CountVectorizer from Scikit-learn.
Merge all selected features into a single feature vector for each movie.
3️⃣ Similarity Calculation
Compute cosine similarity between movie vectors.
When a user inputs a movie title, the system:
Finds the corresponding movie in the dataset.
Retrieves its feature vector.
Calculates similarity scores with all other movies.
Returns the top N most similar movies based on similarity scores.


🔥 Technologies Used
Python
Pandas – For data manipulation and preprocessing
NumPy – For numerical operations
Scikit-learn – For text vectorization (TF-IDF/CountVectorizer) and similarity calculation
NLTK (Natural Language Toolkit) – For text preprocessing and stemming


🚀 Installation & Usage
1️⃣ Install Dependencies
pip install numpy pandas scikit-learn nltk
2️⃣ Load the Dataset
Ensure that movies.csv and credits.csv are placed in your working directory.

3️⃣ Run the Recommender in a Jupyter Notebook
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")
credits = pd.read_csv("credits.csv")

# Preprocessing steps (as implemented in the project)

# Function to get recommendations
def recommend_movies(movie_title):
    # Find similar movies based on cosine similarity
    pass  # Your implementation here

# Example usage
recommend_movies("Inception")
🎯 Example Output
If the user inputs "Inception", the system may return:
1. Interstellar
2. The Prestige
3. Shutter Island
4. Memento
5. The Dark Knight


📌 Future Improvements
✅ Implement collaborative filtering for a hybrid recommendation system.
✅ Improve NLP techniques to enhance text feature extraction.
✅ Deploy as a web application using Flask or Streamlit.
✅ Integrate with a movie database API (like TMDB) for real-time updates.

