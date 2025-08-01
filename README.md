# 🎮 Game Finder – A Smart Steam Game Recommendation System

**Game Finder** is a content-based game recommender system built with **Python**, **NLP**, and **Streamlit**. Instead of requiring users to input specific game names, it allows natural language queries like:

> _"I'm looking for a free open-world multiplayer shooting game with realistic graphics."_

Using **TF-IDF vectorization**, **Porter stemming**, and **cosine similarity**, it finds and recommends the most relevant games from the **Steam store**.

---

## 🧠 What Makes Game Finder Unique?

Unlike traditional recommenders based on user ratings or collaborative filtering, Game Finder focuses on **content-based filtering** using:
- Game name
- Description
- Price

💡 This means it can match any user-provided text — no prior user data needed!

---

## 🕸️ How Data Was Collected

The game data was **scraped directly from Steam** using:
- **Selenium WebDriver** for browser automation
- Navigated to [Steam Top Sellers](https://store.steampowered.com/search/?filter=topsellers)
- Collected:
  - 🎮 Game name
  - 🗓️ Launch date
  - 💰 Price
  - 🖼️ Cover image URL
  - 📝 Short description

> All data is saved into a CSV (`steam_games_with_description.csv`) and used to power the recommender engine.

---

## 🚀 Features

- ✅ Content-based NLP matching using TF-IDF + cosine similarity
- 🧠 Understands natural language game descriptions
- 📦 Local CSV-based game dataset
- 🖥️ Interactive UI with Streamlit
- 🔍 Shows game image, price, date, and description
- 💬 Optional input tuning for number of recommendations

---

## 🛠️ Tech Stack

| Tool         | Purpose                                      |
|--------------|----------------------------------------------|
| Python       | Core programming language                    |
| Streamlit    | Web app UI                                   |
| Selenium     | Data scraping from Steam                     |
| Pandas       | Data handling and manipulation               |
| Scikit-learn | TF-IDF vectorization, cosine similarity      |
| NLTK         | Text preprocessing, stopwords, PorterStemmer |

---

## 💻 Local Setup Instructions

Clone the repository and run the Streamlit app:

```bash
git clone https://github.com/Jatin-GI/Game-Finder.git
cd Game-Finder

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
## 📄 License

[![MIT License](https://img.shields.io/github/license/Jatin-GI/Game-Finder?style=flat-square)](LICENSE)

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙋 Author

**Developed by [Jatin Gupta](https://github.com/Jatin-GI)**  
📫 Email: [guptajatin0416@gmail.com](mailto:guptajatin0416@gmail.com)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/jatin-gupta-b02b37292)

---

## 🌐 Live Demo

[![Streamlit App](https://img.shields.io/badge/🚀%20Launch%20App-Streamlit-green?style=flat-square&logo=streamlit)](https://steamseeker.streamlit.app/)  
> ⚠️ Coming Soon: Replace the link above with your actual app URL once deployed

---

## 📊 Project Stats

![GitHub Repo stars](https://img.shields.io/github/stars/Jatin-GI/Game-Finder?style=social)
![GitHub forks](https://img.shields.io/github/forks/Jatin-GI/Game-Finder?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/Jatin-GI/Game-Finder?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&style=flat-square)

