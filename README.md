# IMDb Movie Analysis Dashboard (2000–2020)

This project analyzes the IMDb Top 1000 movies dataset using Python and visualizes insights using Seaborn & Matplotlib. It’s aimed at preparing data for visualization tools like Power BI or Tableau.

## 📊 Visualizations
- Top 10 genres by average IMDb rating
- Number of movies released per year
- Top 10 directors with the highest average ratings (with ≥3 movies)

## 🧹 Data Cleaning
- Removed unnecessary columns
- Filtered movies between 2000–2020
- Extracted main genre and cleaned null values

## 🗃️ Dataset
- Source: IMDb Top 1000 Movies
- File: imdb_top_1000.csv

## ▶️ How to Run

```bash
pip install -r requirements.txt
python imdb_analysis.py
```

## 🛠️ Tools Used
- Python
- Pandas, Seaborn, Matplotlib
