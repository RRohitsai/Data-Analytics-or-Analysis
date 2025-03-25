import pandas as pd
import matplotlib.pyplot as plt

# Load the IMDb dataset
df = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Pictures\Movie Rating\movies\IMDb Movies India.csv')
print(df.head())

# Ensure column names are cleaned
df.columns = df.columns.str.strip()

# Fixing potential column name issues
rating_col = [col for col in df.columns if 'rating' in col.lower()]
votes_col = [col for col in df.columns if 'votes' in col.lower()]

if rating_col:
    rating_col = rating_col[0]  # Use the correct column name
else:
    raise KeyError("No column found for IMDb Rating")

if votes_col:
    votes_col = votes_col[0]  # Use the correct column name
else:
    raise KeyError("No column found for Votes")

# Convert columns to numeric, handling errors
df[rating_col] = pd.to_numeric(df[rating_col], errors='coerce')
df[votes_col] = pd.to_numeric(df[votes_col], errors='coerce')

# Drop rows with missing values in these columns
df = df.dropna(subset=[rating_col, votes_col])

# Bar Chart: Count of movies by genre
plt.figure(figsize=(6, 4))
df['Genre'].value_counts().head(5).plot(kind='bar', color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Top 5 Movie Genres')
plt.show()

# Pie Chart: Distribution of movie ratings
plt.figure(figsize=(6, 6))
df[rating_col].dropna().astype(int).value_counts().plot(kind='pie', autopct='%1.1f%%', colormap='coolwarm')
plt.title('IMDb Rating Distribution')
plt.ylabel('')
plt.show()

# Line Chart: Yearly movie count
plt.figure(figsize=(6, 4))
df['Year'].value_counts().sort_index().plot(kind='line', color='purple')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.title('Number of Movies Released Per Year')
plt.show()

# Scatter Plot: IMDb Rating vs. Votes
plt.figure(figsize=(6, 4))
plt.scatter(df[rating_col], df[votes_col], color='orange', alpha=0.5)
plt.xlabel('IMDb Rating')
plt.ylabel('Votes')
plt.title('Scatter Plot of IMDb Rating vs Votes')
plt.show()
