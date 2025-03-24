import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df=pd.read_csv(r'C:\Users\Lenovo\OneDrive\Pictures\Titaic\dataset\Titanic-Dataset.csv')
print(df.head())

# Bar Chart: Count of passengers by class
plt.figure(figsize=(6, 4))
df['Pclass'].value_counts().sort_index().plot(kind='bar', color=['blue', 'green', 'red'])
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.title('Passenger Count by Class')
plt.show()

# Pie Chart: Survival distribution
plt.figure(figsize=(6, 6))
df['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red', 'green'], labels=['Did not survive', 'Survived'])
plt.title('Survival Distribution')
plt.ylabel('')
plt.show()

# Line Chart: Age distribution
plt.figure(figsize=(6, 4))
df['Age'].dropna().sort_values().reset_index(drop=True).plot(kind='line', color='purple')
plt.xlabel('Passenger Index')
plt.ylabel('Age')
plt.title('Age Distribution of Passengers')
plt.show()

# Scatter Plot: Age vs. Fare
plt.figure(figsize=(6, 4))
plt.scatter(df['Age'], df['Fare'], color='orange', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Fare Paid')
plt.title('Scatter Plot of Age vs Fare')
plt.show()
