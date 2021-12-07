import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#############################################################################################################################
#############################################################################################################################

def getDataAndNumMovies(movie_data_csv_file): 

    # Read input CSV file as a pandas dataframe
    original_movie_data = pd.read_csv(movie_data_csv_file)

    number_of_movies = 0
    for index, row in original_movie_data.iterrows():
        number_of_movies += 1

    return original_movie_data, number_of_movies

#############################################################################################################################
#############################################################################################################################

def retrieveCleanedData(movie_df): 

    # Clean overviews → lowercasing, stopword removal, punctuation removal
    movie_df.loc[:, "Overview"] = movie_df.loc[:, "Overview"].str.lower()
    movie_df.loc[:, "Genre"] = movie_df.loc[:, "Genre"].str.lower()

    for index, row in movie_df.iterrows():
        overview = row["Overview"].split(" ")
        new_overview = []
        for overview_word in overview:
            if overview_word not in STOP_WORDS: 
                new_overview.append(overview_word)
        row["Overview"] = ' '.join(new_overview)

    for punc in PUNCTUATION: 
        movie_df.loc[:, "Overview"] = movie_df.loc[:, "Overview"].str.replace(punc, "") 

    return movie_df

#############################################################################################################################
#############################################################################################################################

def getTermAndDocFrequency(movie_data): 

    # Set of all unique words, both in the genre and overview columns
    unique_words_set = set()
    for index, row in movie_data.iterrows():
        genres = row["Genre"].split(", ")
        for genre in genres: 
            unique_words_set.add(genre)
        
        overview = row["Overview"].split(" ")
        for word in overview: 
            if (word != ''): 
                unique_words_set.add(word)
    unique_words = list(unique_words_set)

    # Create term frequency nested dictionary for each movie
    term_freqs_per_movie = {}

    # Create  document frequency dictionary for each unique word
    doc_freq_per_unique_word = {}
    # Initialize the document frequencies for each word to 0
    for unique_word in unique_words: 
        doc_freq_per_unique_word[unique_word] = 0

    # Populate term and doc frequency dictionaries
    for index, row in movie_data.iterrows():
        movie = row["Series_Title"]

        movie_term_freq_dict = {}
        unique_words_in_movie = set()

        # Initialize the term frequencies for the movie to 0
        for unique_word in unique_words: 
            movie_term_freq_dict[unique_word] = 0

        genres = row["Genre"].split(", ")
        for genre in genres: 
            unique_words_in_movie.add(genre)
            movie_term_freq_dict[genre] += 1

        overview = row["Overview"].split(" ")
        for overview_word in overview: 
            if (overview_word != ''): 
                movie_term_freq_dict[overview_word] += 1
                unique_words_in_movie.add(overview_word)

        # Add the term frequency dictionary for the movie to the overall dictionary
        term_freqs_per_movie[movie] = movie_term_freq_dict

        for unique_word_in_movie in unique_words_in_movie:
             doc_freq_per_unique_word[unique_word_in_movie] += 1
    
    return unique_words_set, term_freqs_per_movie, doc_freq_per_unique_word

#############################################################################################################################
#############################################################################################################################

def retrieveCleanedQuery(query): 

    # Lowercase
    query = query.lower()

    # Stopword removal
    overview_list = query.split(" ")
    new_overview_list = []
    for overview_word in overview_list:
        if overview_word not in STOP_WORDS: 
            new_overview_list.append(overview_word)
    query = ' '.join(new_overview_list)

    # Punctuation removal
    for punc in PUNCTUATION: 
        query = query.replace(punc, "")

    return query

def getQueryWordCounts(query): 

    query_word_count_dictionary = {}
    query_words = query.split(" ")

    for query_word in query_words: 
        if (query_word not in query_word_count_dictionary): 
            query_word_count_dictionary[query_word] = 1
        else: 
            query_word_count_dictionary[query_word] += 1

    return query_word_count_dictionary

#############################################################################################################################

def rankMoviesGivenQuery(movie_data, query, unique_words_set, term_freqs_per_movie, doc_freq_per_unique_word, number_of_movies): 

    query = retrieveCleanedQuery(query)
    query_word_count_dictionary = getQueryWordCounts(query)
    query_words = query.split(" ")

    movie_ranks = []
    count = 0
    for index, row in movie_data.iterrows():
        movie = row["Series_Title"]
        movie_rank = 0
        for query_word in query_words:
            if (query_word not in unique_words_set): # Word is not in movie data but only in query
                continue
            query_word_count = query_word_count_dictionary[query_word]
            movie_word_count = term_freqs_per_movie[movie][query_word]
            word_doc_freq = doc_freq_per_unique_word[query_word]
            # TF-IDF formula
            movie_rank += (query_word_count * movie_word_count * np.log((number_of_movies + 1)/(word_doc_freq)))
        movie_ranks.append((movie, movie_rank))
        count += 1
    
    # Sort movie ranks
    movie_ranks.sort(key = lambda x: x[1]) 
    movie_ranks.reverse()

    return [tupl[0] for tupl in movie_ranks[0 : NUM_MOVIES_TO_RANK]]

#############################################################################################################################
#############################################################################################################################

PUNCTUATION = [".", "-", "_", ",", "?", "!", "'", "\"", "\`", "*", "@", "#", "$", "%", "^", "&", "(", ")", "/", "\\", "\+"]
stopwords_file = open("stopwords.txt", "r")
STOP_WORDS = stopwords_file.read().splitlines()
DEFAULT_WORD_COUNT = 1
NUM_MOVIES_TO_RANK = 5

def searchEngineRecommendMovies(inputQuery): 
    original_movie_data, number_of_movies = getDataAndNumMovies("movie_data.csv")
    movie_data = retrieveCleanedData(original_movie_data)
    unique_words_set, term_freqs_per_movie, doc_freq_per_unique_word = getTermAndDocFrequency(movie_data)
    ranked_movies = rankMoviesGivenQuery(movie_data, inputQuery, unique_words_set, term_freqs_per_movie, doc_freq_per_unique_word, number_of_movies)
    return ranked_movies
