import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load the sheet
df=pd.read_csv("netflix_data.csv")
print("initilal data :\n",df)

# Extract duration in minutes (for movies)
df['Duration_mins'] = df['Duration'].str.extract('(\d+)').astype(float)
print(df)
# seperate movies and tv shows
movies = df[df["Type"] == "Movie"]
tv_shows = df[df["Type"] == "TV Show"]

# visualize with matplotlib

# comparing movies and tv shows 
counts=df["Type"].value_counts()
print(counts)
plt.figure(figsize=(6,4))
plt.bar(counts.index,counts.values,color=['red','blue'])
plt.title("Content Type Distribution")
plt.ylabel("Count")
plt.savefig('plots/type_distribution.png')
plt.show()

#movie duration comparision 
plt.figure(figsize=(8,5))
plt.bar(movies["Title"],movies["Duration_mins"],color='green')
plt.xticks(rotation=45)
plt.title('movie Duration Comparision')
plt.ylabel('Duration (minutes)')
plt.tight_layout()
plt.savefig('plots/movie_duration.png')
plt.show()

#content by country
counts1=df['Country'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(counts1.index,counts1.values,color='red')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.title('Content by country')
plt.tight_layout()
plt.savefig('plots/country_count.png')
plt.show()





