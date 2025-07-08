import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("imdb_top_1000.csv")

# Drop irrelevant columns
columns_to_drop = ['Poster_Link', 'Certificate', 'Overview', 'Meta_score', 'Gross']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Handle missing values
df.dropna(subset=['IMDB_Rating', 'Genre', 'Released_Year'], inplace=True)

# Convert data types
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')

# Filter years for analysis (2000–2020)
df = df[(df['Released_Year'] >= 2000) & (df['Released_Year'] <= 2020)]

# Extract main genre
df['Main_Genre'] = df['Genre'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else x)

# Plot: Top 10 Genres by Average IMDB Rating
plt.figure(figsize=(10, 6))
top_genres = df.groupby('Main_Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, palette='mako')
plt.title("Top 10 Genres by Average IMDB Rating (2000–2020)")
plt.xlabel("Average IMDB Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# Plot: Movies Released Per Year
plt.figure(figsize=(12, 6))
yearly_counts = df['Released_Year'].value_counts().sort_index()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o')
plt.title("Number of Movies Released Per Year (2000–2020)")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()

# Plot: Top 10 Directors by Average Rating (with at least 3 movies)
top_directors = df.groupby('Director').filter(lambda x: len(x) >= 3)
avg_ratings = top_directors.groupby('Director')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_ratings.values, y=avg_ratings.index, palette='rocket')
plt.title("Top 10 Directors by Average IMDB Rating (min 3 movies)")
plt.xlabel("Average Rating")
plt.ylabel("Director")
plt.tight_layout()
plt.show()

# Save cleaned data
df.to_csv("cleaned_imdb_data.csv", index=False)
