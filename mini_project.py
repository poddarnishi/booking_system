# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from datetime import datetime
import matplotlib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movie = pd.DataFrame(pd.read_excel('Mini_Project_Sample_Data.xlsx'))
del movie['movie_release_date']
movie['movie_name']=movie['movie_name'].astype(str)
movie

'''movie.describe()

#Frequency of Movie Ratings (IMDb)
plt.figure(figsize = (12, 8))
sns.set_theme(style = "whitegrid")
ax = sns.countplot(x = 'rating', data = movie, palette = 'rainbow')
plt.title("Frequency of Ratings", fontsize = 20)
plt.xlabel("Ratings", fontsize = 15)
plt.ylabel("Count", fontsize = 15)
plt.show()

cmap = plt.get_cmap('copper')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]
explode = [0.1, 0, 0.1, 0, 0.1, 0]
plot = movie.plot.pie(y = 'movie_duration', autopct = '%1.1f%%', explode = explode, labels = movie.genre, fontsize = 15, figsize = (12, 8), shadow = True, colors = colors)

corr = movie.corr()
plt.figure(figsize = (12, 8))
#vmax - limit
sns.heatmap(corr, vmax = .4, square = True)
plt.title('Correlation matrix') '''

upcoming_movies = pd.DataFrame(pd.read_excel('Upcoming_movies.xlsx'))
#separates month from movie_release_date
upcoming_movies['month_date'] = upcoming_movies['movie_release_date'].dt.strftime('%m')
upcoming_movies.head()
'''
#Genre distribution of Movie Dataset
plt.figure(figsize = (12, 8))
sns.set_theme(style = "whitegrid")
ax = sns.countplot(x = 'genre', data = upcoming_movies, palette = 'viridis')
plt.title('Genre distribution', fontsize = 20)
plt.ylabel('Frequency', fontsize = 15)
plt.xlabel('Genre', fontsize = 15)
plt.show()

#Frequency of Movies per month
plt.figure(figsize = (12, 8))
sns.set_theme(style = "whitegrid")
ax = sns.countplot(x = 'month_date', data = upcoming_movies, palette = 'Set2')
plt.title("Upcoming Movies Monthly", fontsize = 20)
plt.xlabel("Months", fontsize = 15)
plt.ylabel("Movies", fontsize = 15)
plt.show() '''
#Most no. of movies released in April

movie = movie[['movie_id', 'movie_name', 'genre']]
upcoming_movies = upcoming_movies[['movie_id', 'movie_name', 'genre']]
movie = movie.append(upcoming_movies, sort = False)
movie.head() 

#Content-based filtering
#recommendations on the basis of genre
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2), min_df = 0, stop_words = 'english')
tfidf_matrix = tf.fit_transform(movie['genre'])
#calculates numeric quantity i.e. the similarity between two movies
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
#linear_kernel calculates the dot product to give cosine_score
titles = movie['movie_name']
indices = pd.Series(movie.index, index = movie['movie_name'])

# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(movie_name):
    idx = indices[movie_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    final_rec = titles.iloc[movie_indices].to_list()
    return final_rec

