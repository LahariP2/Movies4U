
**Progress Report**

Lahari Pisupati, Grace Im, Shivani Ingle, Crystal Wang


**Tasks:** 
     
      Clean dataset → remove unnecessary columns - 2 hours
      Stop word removal in movie descriptions - 2 hours
      Clean overviews → lowercasing, stopword removal, punctuation removal, split genres - 2 hours
      Write code to create a topic model - 10 hours
      Train the model - 2 hours
      Testing accuracy of topic model output - 2 hours
      Debugging and fixing errors for the topic model - 2 hours
      Implement TF-IDF ranking algorithm for search engine - 8 hours
      Implement Query Likelihood ranking algorithm for search engine - 8 hours
      Testing and comparing accuracy of both ranking models - 5 hours
      Write underlying Chrome Extension code - 5 hours
      Integrate topic model & ranking code into the Chrome Extension code - 8 hours
      Create UI design - 6 hours
      Implement UI design - 8 hours
      Debugging and fixing errors for the search engine - 5 hours
      Cleaning up code, writing comments - 5 hours



 
**1) Which tasks have been completed?**

We found four different datasets that are related to IMDB movies; movies, names, rating and title principal. 

During the process of dataset cleaning, we decided to create a new dataset by selecting essential data from each dataset 

that is relevant for our project. Since our project focuses on returning movie genres and suggestions based on the inputted summary,

we selected data columns such as movie title, genre, IMDB rating, and total number of votes received. 

We also loaded the dataset and wrote a program to remove any stop words in the movie descriptions/overviews. 

We further cleaned the movie descriptions data by tokenizing the text and removing punctuations. 

For topic modeling we decided to use Latent Dirichlet Allocation (LDA), to transform the textual data in a format that 

serves as an input for training the LDA model. We used the previously written function that cleans the movie data in order to 

create a tokenized object. Next we converted the tokenized object into a corpus and dictionary. We trained the model with the number

of topics equal to the number of genres in the dataset. We finally used a visualization package pyLDAvis to visualize the topic model. 




**2) Which tasks are pending?**

As can be seen in the tasks list above, we have completed tasks 1-5, which are the core structure of the topic model, 

and we still have to complete tasks 6-16. These remaining tasks involve testing our topic model and fixing any bugs 

(we might need to try out different topic model algorithms depending on our current results), implementing the main 

portion of the search engine with TF-IDF and Query Likelihood, and developing our Chrome Extension application.  




**3) Are you facing any challenges?**

While implementing the topic model, we had some trouble with categorizing words that show up in multiple different topic 

categories. To fix this, we had to keep track of the number of occurrences of each word per topic. Then, we assigned the word 

to a topic for which the word occurred the most in. Another challenge we are currently facing is testing the accuracy of the 

topic model output given that some movies can be classified into various topics/genres. In such situations, we are trying to 

figure out if we will output the genre that most likely describes the movie or output all genres that the movie fits into. 




