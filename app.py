import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

# Download stopwords
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("steam_games.csv")
df.fillna('', inplace=True)

# Preprocessing tools
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    tokens = text.split()
    tokens = [stemmer.stem(w) for w in tokens if w not in stop_words]
    return ' '.join(tokens)

# Combine metadata
df['combined'] = (
    df['Game Name'] + ' ' +
    df['Price'].astype(str) + ' ' +
    df['Description']
).apply(preprocess)

# Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Recommendation function
def recommend_from_text(user_input, top_n=5):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    
    recommendations = []
    for i in top_indices:
        recommendations.append({
            "Game Name": df.iloc[i]['Game Name'],
            "Price": df.iloc[i]['Price'],
            "Launch Date": df.iloc[i]['Launch Date'],
            "Image": df.iloc[i]['Image'],
            "Description": df.iloc[i]['Description'][:300] + '...'
        })
    return recommendations

# ---------------------- STREAMLIT UI ----------------------
st.set_page_config(page_title="Steam Game Recommender", layout="centered")
st.title("🎮 Steam Game Recommender")
st.write("Describe what kind of game you’re looking for and get top recommendations!")

user_query = st.text_area("🧠 Enter your game preferences (e.g., 'free multiplayer shooter with great graphics')", height=100)

top_n = st.slider("Number of recommendations", min_value=1, max_value=10, value=5)

if st.button("🔍 Recommend"):
    if user_query.strip() == "":
        st.warning("Please enter a description.")
    else:
        with st.spinner("Finding the best matches..."):
            results = recommend_from_text(user_query, top_n)
            for game in results:
                st.subheader(game['Game Name'])
                st.markdown(f"**🗓️ Launch Date:** {game['Launch Date']}")
                st.markdown(f"**💰 Price:** {game['Price']}")
                st.markdown(f"**📝 Description:** {game['Description']}")
                st.image(game['Image'], width=300)
                st.markdown("---")
