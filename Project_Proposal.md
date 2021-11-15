1. **What are the names and NetIDs of all your team members? Who is the captain? The captain will have more administrative duties than team members.**
      
      TEAM CAPTAIN - Lahari Pisupati - lahari2
      
      Grace Im - youjini2
      
      Crystal Wang - cw30
      
      Shivani Ingle - ingle3

2. **What is your free topic? Please give a detailed description. What is the task?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our application has two features, a topic model and a search engine. 
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<ins>Topic model</ins>: Users can input a summary of a specific movie and we will tell them the genre of the movie based on the inputted summary. 
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<ins>Search engine</ins>: Users browsing for movie suggestions can enter queries that describe a specific movie, theme or storyline, and we will give them a ranked movie list of recommendations. 

    **Why is it important or interesting?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our application has a practical use for people looking for new movie suggestions or interested in filtering out movies based on the genre. 	

    **What is your planned approach?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First, we will work on parsing and cleaning the dataset. 
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then, we'll implement the algorithms taught in class to train a topic model that recognizes & classifies movies into different genres. 
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will implement a search engine system using various TF-DIF and other techniques to rank movies based on the inputted query.
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will integrate the topic model and search engine with backend methods to fetch data based on user input.
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Finally, we will create a Chrome Extension to enable easy user usage. 

    **What tools, systems or datasets are involved?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We are going to use the Chrome API to create a Chrome extension
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We are using the movies dataset includes 85,855 movies with attributes such as movie description, average rating, number of votes, and genre. Data has been scraped from the publicly available website https://www.imdb.com. All the movies with more than 100 votes have been scrapped as of 01/01/2020.

    **What is the expected outcome?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We expect to output the movie genre that is relevant to the user's movie summary input and rank movies based on the inputted query.  

    **How are you going to evaluate your work?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will evaluate our work by running our dataset as input and using statistical tests to ensure the results are not random. 
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will also have various peer reviewers test our application with different input

 3. **Which programming language do you plan to use?**
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python, Javascript, HTML

4. **Please justify that the workload of your topic is at least 20*N hours, N being the total number of students in your team. You may list the main tasks to be completed, and the estimated time cost for each task.**
      
      *_Below are the approximations for the amount of time to complete main tasks. Approximations may change as we start working on the project._  
        
        Clean dataset, remove unnecessary columns - 2 hours
        Stop word removal in movie descriptions - 2 hours
        Clean overviews: stopword/punctuation removal, tokenization, lowercasing - 2 hours
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


