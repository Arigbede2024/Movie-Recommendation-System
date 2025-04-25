# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and Pandas. This project suggests movies similar to a given title based on their genres, keywords, cast, and crew.

## 🚀 Features

- Recommend similar movies based on content similarity
- Preprocessed and cleaned movie metadata
- Cosine similarity for recommendations
- Built with a lightweight UI using Streamlit (optional)
- Uses a reduced dataset (1,000 movies) for performance

## 🧠 How It Works

1. **Data Cleaning & Preprocessing**:
   - Merged movie metadata with keywords and credits
   - Extracted important features (title, genres, overview, etc.)
   - Created a `tags` column combining all useful info

2. **Feature Engineering**:
   - Tokenization, stemming, and vectorization of tags
   - Converted text data into numerical vectors using CountVectorizer
   - Calculated similarity using cosine distance

3. **Recommendation Logic**:
   - Given a movie title, return top 5/10 most similar movies

## 🛠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- NLTK
- Streamlit 

## 📁 Project Structure


## 🧪 How to Run

### 1. Clone the Repository

`bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

pip install -r requirements.txt

[streamlit link](https://movie-recommention2025.streamlit.app/)


### 2. Notes


Dataset is reduced to 1,000 movies for speed and demo purposes

Can be scaled to full dataset with optimization


🙌 Contributing
Feel free to fork, open issues, or submit pull requests!


📃 License
MIT License


Made with 💡 and 🎥 by Arigbede Bukola

---



