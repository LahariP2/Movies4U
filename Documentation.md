**Progress Documentation**


**Overview of the function of the code:**

The function of our code is to output the genre of the movie that matches best to the query users enter into the search bars and/or a list of top 5 recommended movies based on their ranking. Users could enter a title, summary, theme, or storyline of their choice. Our software can be used for looking up the genre of a movie based on the title or find new movie recommendations to watch. It can also be used for searching the title of the movie that the user does not recollect but remembers bits and pieces of the movie.


**Implementation of the software:**

We initially cleaned the dataset and removed the stopwords like “and”, ”you”, ”by”, etc. in order to give more weightage to important and unique words. We further cleaned the data of the movie descriptions by removing punctuations, lowercasing text, and such. We then found the unique genres and then converted it to a list so as to map each genre to its row index in the topic model dataframe. Similarly, we found the unique words in the entire dataset. We implemented a unigram language model based MLE algorithm to estimate the probabilities of generating words for each genre. We further used Bayesian estimation/inference to associate each document with a probability distribution over topics. We found the probability of the word in the document, and then normalized these probabilities such that the p(w|genre) = 1. Based on the number of times the words in the query occured in a document, we ranked these documents and outputted the results. For the search engine, we obtained the unique genres and words, created the TF and IDF matrices, and implemented the TF-IDF ranking algorithm in order to rank movies. 


**How to Run the Software:**

To install and run the software, first we need to git clone from GitHub Repository. Open terminal and change the current working directory to the location directory where you want to clone the repository. 
      Git clone https://github.com/LahariP2/Movies4U.git
After cloning into your local directory, you can run
      export FLASK_APP=movies4u
      flask run
To run in debug mode, type the following before flask run
      export FLASK_ENV=development
After running the above command lines, copy, paste, and go to the link: http://127.0.0.1:5000/
You will be able to see a web page with two search bars. The information you entered into the first search bar will output the overview of the movie and genre, while the second search bar will generate a list of the top 5 ranked movies based on your search. 


**Contribution of each member:**

*Lahari Pisupati:* Implemented the Topic model using the Maximum Likelihood estimation method. Wrote helper methods to clean data, obtain unique words and unique genres, and create the topic model dataframe. Developed the classifier using the Naive Bayes algorithm, by obtaining the prior probabilities and probabilities that each word belongs to each genre. Also, implemented the Search Engine using the TF-IDF algorithm to rank movies based on the inputted query. Once again, I wrote helper methods to obtain unique words and unique genres, and to fill out the TF and IDF matrices, which I then used to rank movies based on the query words. For both the topic model classifier and search engine, I wrote methods to test accuracies and iteratively improved algorithms. 


*Grace Im:* Data cleaning (stopword and punctuation removal), ReadMe file documentation, final presentation documentation, final documentation, data research 


*Shivani Ingle:* TF IDF algorithm, powerpoint presentation, final documentation


*Crystal Wang:* final documentation, final presentation, data research


