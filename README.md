## Movies4U

# Overview
Our team’s project focuses on topic modeling and search engine optimization. Our application has a practical use for people looking to classify movies into genres, interested in filtering out movies based on a description, or looking for new movie recommendations. We implemented two features, a topic model and a search engine. The users can input a summary, theme or storyline of a movie they are interested in. We will browse through our dataset which contains information on the title, rating, overview and rating of the movie. Using our code, the output would be the genre of the movie or a list of the recommended movies. 

# Tool & Dataset
We used the Flask framework to create a Flask web application. We used the movies dataset includes 85,855 movies with attributes such as movie description, average rating, number of votes, and genre. Data has been scraped from the publicly available website https://www.imdb.com. All the movies with more than 100 votes have been scrapped as of 01/01/2020. During the process of dataset cleaning, we decided to delete unnecessary columns and select data columns such as movie title, genre, IMDB rating, overview and total number of votes received. We also loaded the dataset and wrote a program to remove any stop words in the movie descriptions/overviews. We further cleaned the movie descriptions data by tokenizing the text and removing punctuations. 

# How it works
The function of our code is to output the genre of the movie that matches best to the query users enter into the search bars and/or a list of recommended movies based on the user's query. Users could enter a title, summary, theme, or storyline of their choice. Our software can be used for looking up the genre of a movie based on the title or to look for new movie recommendations to watch. It can also be used for searching the title of the movie that the user forgot. 

# Implementation
We initially cleaned the dataset and removed the stopwords like “and”, ”you”, ”by”, etc. in order to give more weightage to important and unique words. We further cleaned the data of the movie descriptions by removing punctuations, lowercasing letters, and such. 
For the topic model, we  found the unique genres and then converted it to a list so as to map each genre to its row index in the topic model dataframe. We implemented the MLE method to obtain the probability that each word can come from each movie genre. We further used Bayesian estimation/inference to associate each document with a probability distribution over topics. We found the probability of the word in the document, and then normalized these probabilities such that the p(w|genre) = 1. Based on the number of times the words in the query occured in a document, we ranked these documents and outputted the results.
For the search engine, we implemented helper methods to find unique genres and words, and ranked movies based on the TF-IDF ranking algorithm. 

# How to run the program
1. To install and run the software, first we need to git clone from GitHub Repository. Open terminal and change the current working directory to the location directory where you want to clone the repository. 
2. Git clone https://github.com/LahariP2/Movies4U.git
3. After cloning into your local directory, you can run
  ```export FLASK_APP=movies4u```
  ```flask run```
4. If you run into a WARNING: This is a development server. Run this command line:
  ```export FLASK_ENV=development before flask run```
5. After running the above command lines, copy, paste, and go to the link: http://127.0.0.1:5000/
You will be able to see a web page with two search bars. The information you entered into the first search bar will output the overview of the movie and genre, while the second search bar will generate a list of the top 5 ranked movies based on your search. 

