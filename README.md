# 🎬 Movie Recommendation System

This project is a Movie Recommendation System built using Python and Streamlit. It combines **Collaborative Filtering** and **Content-Based Filtering** techniques to suggest personalized movie recommendations based on user preferences.

## 📌 Features

- Suggests Top 5 movies similar to user’s choice
- Two filtering methods:
  - Collaborative Filtering (based on user ratings)
  - Content-Based Filtering (based on genres)
- Interactive web UI using Streamlit
- Real-world dataset: [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)
- Clean, modular code structure
- Extensible for future improvements like sentiment analysis

## 🛠 Tools & Technologies

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **MovieLens 100K dataset**

## 🚀 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
```

2. **Install requirements**
```bash
pip install -r requirements.txt
```

3. **Run Streamlit app**
```bash
streamlit run app.py
```

## 📁 Project Structure

```
movie-recommendation-system/
├── app.py                      # Streamlit UI script
├── recommendation.ipynb       # Jupyter notebook with logic
├── movielens/                 # Folder with u.data and u.item
├── Movie_Recommendation_System_Report.pdf
└── README.md
```

## 📄 Report

A detailed 2-page project report is included:  
**➡️ [Movie_Recommendation_System_Report.pdf](./Movie_Recommendation_System_Report.pdf)**

## 📬 Contact

**Dinesh Karthik Nayak**  
📧 dineshnayak2436@gmail.com

## 📌 Future Scope

- Add sentiment-based filtering using reviews
- Include user login and profile tracking
- Deploy app using Streamlit Cloud or Heroku

## ⭐ License

This project is open-source and free to use under the [MIT License](LICENSE)
