import pandas as pd
import numpy as np

def retrieveCleanedData(movie_data_csv_file): 
    original_movie_data = pd.read_csv(movie_data_csv_file)
    movie_data = original_movie_data.loc[:, ["Genre", "Overview"]]

    # Clean overviews → lowercasing, stopword removal, punctuation removal
    movie_data.loc[:, "Overview"] = movie_data.loc[:, "Overview"].str.lower()

    stopwords_file = open("stopwords.txt", "r")
    stop_words = stopwords_file.read().splitlines()

    for index, row in movie_data.iterrows():
        overview = row["Overview"].split(" ")
        new_overview = []
        for i in range(len(overview)): 
            overview_word = overview[i]
            if overview_word not in stop_words: 
                new_overview.append(overview_word)
        row["Overview"] = ' '.join(new_overview)

    PUNCTUATION = [".", "-", "_", ",", "?", "!", "'", "\"", "\`", "*", "@", "#", "$", "%", "^", "&", "(", ")", "/", "\\", "\+"]

    for punc in PUNCTUATION: 
        movie_data.loc[:, "Overview"] = movie_data.loc[:, "Overview"].str.replace(punc, "") 

    # Split genres → If a movie is classified under multiple genres, split the genres into their own rows with same overview
    genre_overview = pd.DataFrame()
    for index, row in movie_data.iterrows():
        genres = row["Genre"].split(", ")
        for genre in genres: 
            row["Genre"] = genre
            genre_overview = genre_overview.append(row, ignore_index = True)

    return genre_overview

#############################################################################################################################

def getUniqueGenres(genre_overview): 
    # Set of all unique genres, later converted to a list
    unique_genres = set()
    for index, row in genre_overview.iterrows():
        genre = row["Genre"]
        unique_genres.add(genre)
    unique_genres = list(unique_genres)

    # Map of each genre to its row index in the topic model dataframe 
    genre_index_map = {}
    index = 0
    for genre in unique_genres: 
        genre_index_map[genre] = index
        index += 1

    return unique_genres, genre_index_map

def getUniqueWords(genre_overview): 
    # Set of all unique words, later converted to a list
    unique_words = set()
    for index, row in genre_overview.iterrows():
        overview = row["Overview"].split(" ")
        for word in overview: 
            if (word != ''): 
                unique_words.add(word)
    unique_words = list(unique_words)

    # Map of each word to its column index in the topic model dataframe 
    word_index_map = {}
    index = 2
    for word in unique_words: 
        word_index_map[word] = index
        index += 1

    return unique_words, word_index_map

def initializeTopicModelAsArray(unique_genres, unique_words): 

    # Add two columns for the genre ID and the total number of words per genre
    column_names = ["genreID", "wordsPerGenre"]
    column_names.extend(list(unique_words))
    topic_model_array = np.zeros((len(unique_genres), 2 + len(unique_words)))
    for i in range(len(unique_genres)): 
        topic_model_array[i, 0] = i
    return column_names, topic_model_array    

#############################################################################################################################

# Convert word and genre counts to probabilities
def convertToProbability(topic_model_counts): 
    for row_idx in range(len(topic_model_counts)):
        wordsPerGenre = topic_model_counts[row_idx, 1]
        for col_idx in range(2, topic_model_counts.shape[1]): 
            topic_model_counts[row_idx, col_idx] /= wordsPerGenre
    return topic_model_counts

def normalizeTopicModelProbabilities(topic_model_probs_array): 
    for row_idx in range(topic_model_probs_array.shape[0]): 
        norm = np.linalg.norm(topic_model_probs_array[row_idx])
        topic_model_probs_array[row_idx] /= norm
    return topic_model_probs_array

def generateTopicModel(genre_overview): 

    unique_genres, genre_index_map = getUniqueGenres(genre_overview)
    unique_words, word_index_map = getUniqueWords(genre_overview)
    column_names, topic_model_counts = initializeTopicModelAsArray(unique_genres, unique_words)

    # For every genre, count the total number of times every word appears in it
    for index, row in genre_overview.iterrows():
        genre = row["Genre"]
        genre_id = genre_index_map[genre]
        overview = row["Overview"].split(" ")
        topic_model_counts[genre_id, 1] += len(overview) # "wordsPerGenre"
        for word in overview: 
            if (word != ''): 
                word_id = word_index_map[word]
                topic_model_counts[genre_id, word_id] += 1

    topic_model_probs_array = convertToProbability(topic_model_counts)
    
    non_norm_topic_model = pd.DataFrame(topic_model_probs_array, columns = column_names)

    normalized_topic_model_array = normalizeTopicModelProbabilities(topic_model_probs_array)
    topic_model = pd.DataFrame(normalized_topic_model_array, columns = column_names)

    return non_norm_topic_model, topic_model

#############################################################################################################################

genre_overview = retrieveCleanedData("movie_data.csv")
topic_model = generateTopicModel(genre_overview)
