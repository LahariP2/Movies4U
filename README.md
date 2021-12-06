## Movies4U

# Overview
Our team’s project focuses on topic modeling and search engine optimization. Our application has a practical use for people looking for new movie suggestions, interested in filtering out movies based on the genre or if they are trying to find the movie based on the description. We implemented two features, a topic model and a search engine. The users can input a summary, theme or storyline of a movie they are interested in. We will browse through our dataset which contains information on the title, rating, overview and rating of the movie. Using our code, the output would be the genre of the movie and a list of the recommended movies based on the IMDB ranking of the movies. 

# Tool & Dataset
We are going to use the Chrome API to create a Chrome extension. We are using the movies dataset includes 85,855 movies with attributes such as movie description, average rating, number of votes, and genre. Data has been scraped from the publicly available website https://www.imdb.com. All the movies with more than 100 votes have been scrapped as of 01/01/2020. During the process of dataset cleaning, we’ve decided to delete unnecessary columns and select data columns such as movie title, genre, IMDB rating, overview and total number of votes received. We also loaded the dataset and wrote a program to remove any stop words in the movie descriptions/overviews. We further cleaned the movie descriptions data by tokenizing the text and removing punctuations. 

# How it works
The function of our code is to output a list of recommended movies based on their ranking and/or the genre of the movie that matches best to the query users enter into the search bars. Users could enter a title, summary, theme, or storyline of their choice. Our software can be used for looking up the genre of a movie based on the title or to look for new movie recommendations to watch. It can also be used for searching the title of the movie that the user forgot. 

# Implementation
Unigram
