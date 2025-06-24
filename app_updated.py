
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def load_data():
    ratings = pd.read_csv("ml-100k/ml-100k/u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
    movies = pd.read_csv(
        "ml-100k/ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        header=None,
        names=[
            "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
            "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
            "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
            "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
        ],
        usecols=["movie_id", "title", "Action", "Comedy", "Drama", "Romance", "Thriller"]
    )
    df = pd.merge(ratings, movies, on="movie_id")
    return df

def create_user_movie_matrix(df):
    return df.pivot_table(index='user_id', columns='title', values='rating')

def get_collaborative_recommendations(title, df, n=5):
    matrix = create_user_movie_matrix(df)
    movie_ratings = matrix.fillna(0).T
    similarity = cosine_similarity(movie_ratings)
    similarity_df = pd.DataFrame(similarity, index=movie_ratings.index, columns=movie_ratings.index)
    if title not in similarity_df:
        return []
    similar_movies = similarity_df[title].sort_values(ascending=False)[1:n+1]
    return similar_movies.index.tolist()

def get_content_based_recommendations(fav_title, df, n=5):
    genre_cols = ["Action", "Comedy", "Drama", "Romance", "Thriller"]
    genre_map = df.drop_duplicates("title")[["title"] + genre_cols]
    genre_map["genre_str"] = genre_map[genre_cols].astype(str).agg("".join, axis=1)
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(genre_map["genre_str"])
    similarity = cosine_similarity(genre_matrix)
    sim_df = pd.DataFrame(similarity, index=genre_map['title'], columns=genre_map['title'])
    if fav_title not in sim_df:
        return []
    return sim_df[fav_title].sort_values(ascending=False)[1:n+1].index.tolist()

df = load_data()
st.title("🎬 Movie Recommendation System")

movie_list = sorted(df['title'].unique())
selected_movie = st.selectbox("Select a movie you like:", movie_list)

method = st.radio("Choose recommendation method:", ["Collaborative Filtering", "Content-Based Filtering"])

if st.button("Get Recommendations"):
    if method == "Collaborative Filtering":
        results = get_collaborative_recommendations(selected_movie, df)
    else:
        results = get_content_based_recommendations(selected_movie, df)

    if results:
        st.subheader("Top 5 Recommended Movies:")
        for i, movie in enumerate(results, 1):
            st.write(f"{i}. {movie}")
    else:
        st.warning("No recommendations found. Try another movie.")
