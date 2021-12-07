import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#############################################################################################################################
#############################################################################################################################

def getTrainTestSplitAsDFFromDF(movie_data_csv_file): 

    # Read input CSV file as a pandas dataframe
    original_movie_data = pd.read_csv(movie_data_csv_file)
    genre_overview_df = original_movie_data.loc[:, ["Genre", "Overview"]]

    # Split the genre overview dataframe into 80-20 train-test split
    genres = genre_overview_df["Genre"].tolist()
    overviews = genre_overview_df["Overview"].tolist()
    overview_train, overview_test, genre_train, genre_test = train_test_split(overviews, genres, test_size = 0.33, random_state = 42)

    train_data_array = np.column_stack((genre_train, overview_train))
    train_genre_overviews_df = pd.DataFrame(train_data_array, columns = ["Genre", "Overview"])

    return train_genre_overviews_df, overview_train, overview_test, genre_train, genre_test

#############################################################################################################################
#############################################################################################################################

def retrieveCleanedData(genre_overview_df): 

    # Clean overviews → lowercasing, stopword removal, punctuation removal
    genre_overview_df.loc[:, "Overview"] = genre_overview_df.loc[:, "Overview"].str.lower()

    for index, row in genre_overview_df.iterrows():
        overview = row["Overview"].split(" ")
        new_overview = []
        for overview_word in overview:
            if overview_word not in STOP_WORDS: 
                new_overview.append(overview_word)
        row["Overview"] = ' '.join(new_overview)

    for punc in PUNCTUATION: 
        genre_overview_df.loc[:, "Overview"] = genre_overview_df.loc[:, "Overview"].str.replace(punc, "") 

    # Split genres → If a movie is classified under multiple genres, split the genres into their own rows with same overview
    genre_overview = pd.DataFrame()
    for index, row in genre_overview_df.iterrows():
        genres = row["Genre"].split(", ")
        for genre in genres: 
            row["Genre"] = genre
            genre_overview = genre_overview.append(row, ignore_index = True)

    return genre_overview

#############################################################################################################################
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

    # Create topic model array and initialize genre indices
    topic_model_array = np.zeros((len(unique_genres), 2 + len(unique_words)))
    for i in range(len(unique_genres)): 
        topic_model_array[i, 0] = i

    return column_names, topic_model_array    

def convertToProbability(topic_model_counts): 

    # Convert word and genre counts to probabilities
    for row_idx in range(len(topic_model_counts)):
        wordsPerGenre = topic_model_counts[row_idx, 1]
        if (wordsPerGenre == 0): 
            continue
        for col_idx in range(2, topic_model_counts.shape[1]): 
            topic_model_counts[row_idx, col_idx] /= wordsPerGenre
            if (topic_model_counts[row_idx, col_idx] == 0): 
                topic_model_counts[row_idx, col_idx] = DEFAULT_PROBABILITY

    return topic_model_counts

def normalizeTopicModelProbabilities(topic_model_probs_array): 

    # Normalize probabilities
    for col_idx in range(topic_model_probs_array.shape[1]): 
        norm = np.linalg.norm(topic_model_probs_array[:, col_idx])
        topic_model_probs_array[:, col_idx] /= norm

    return topic_model_probs_array

#############################################################################################################################

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
                topic_model_counts[genre_id, word_id] += WORD_WEIGHT

    # Convert the counts to probabilities and normalize the probabilities
    topic_model_probs_array = convertToProbability(topic_model_counts)
    normalized_topic_model_array = normalizeTopicModelProbabilities(topic_model_probs_array)
    topic_model = pd.DataFrame(normalized_topic_model_array, columns = column_names)

    return unique_genres, genre_index_map, unique_words, word_index_map, topic_model

#############################################################################################################################
#############################################################################################################################

def retrieveCleanedInputOverview(input_overview): 

    # Lowercase
    input_overview = input_overview.lower()

    # Stopword removal
    overview_list = input_overview.split(" ")
    new_overview_list = []
    for overview_word in overview_list:
        if overview_word not in STOP_WORDS: 
            new_overview_list.append(overview_word)
    input_overview = ' '.join(new_overview_list)

    # Punctuation removal
    for punc in PUNCTUATION: 
        input_overview = input_overview.replace(punc, "")

    return input_overview
    
def probsOfOverviewPerGenre(input_overview, unique_genres, genre_index_map, unique_words, topic_model): 
    
    # Initialize all probabilities to 1
    num_unique_genres = len(unique_genres)
    probabilitiesPerGenre = [DEFAULT_PROBABILITY] * num_unique_genres 

    # Get the probabilitiy that each word appears in each genre
    overview_words_list = input_overview.split(" ")
    for word in overview_words_list: 
        if word not in unique_words: 
            continue
        for genre in unique_genres: 
            genre_id = genre_index_map[genre]
            probWordInGenre = topic_model.at[genre_id, word]
            probabilitiesPerGenre[genre_id] *= probWordInGenre

    return probabilitiesPerGenre

#############################################################################################################################

def classifyMovieOverview(input_overview, unique_genres, genre_index_map, unique_words, topic_model): 

    # Clean input overview and get the probabilities that the overview is generated from each genre
    input_overview = retrieveCleanedInputOverview(input_overview)
    probabilitiesPerGenre = probsOfOverviewPerGenre(input_overview, unique_genres, genre_index_map, unique_words, topic_model)

    # Sort the genre probabilities and return the top three most likely genres (if applicable) that the input overview can be classified into
    num_unique_genres = len(unique_genres)
    asc_genre_probs = np.argsort(probabilitiesPerGenre)
    desc_genre_probs = asc_genre_probs[::-1][:num_unique_genres]

    if (probabilitiesPerGenre[desc_genre_probs[1]] == 0): 
        return unique_genres[desc_genre_probs[0]]
    elif (probabilitiesPerGenre[desc_genre_probs[2]] == 0): 
        return unique_genres[desc_genre_probs[0]], unique_genres[desc_genre_probs[1]]

    return [unique_genres[desc_genre_probs[0]], unique_genres[desc_genre_probs[1]], unique_genres[desc_genre_probs[2]]]

#############################################################################################################################
#############################################################################################################################

def testModelAccuracy(overview_test, genre_test, unique_genres, genre_index_map, unique_words, topic_model): 
    i = 0
    correct = 0
    for overview in overview_test: 
        movie_genre = classifyMovieOverview(overview, unique_genres, genre_index_map, unique_words, topic_model)
        correct_genres = (genre_test[i]).split(", ")
        if (movie_genre in correct_genres): 
            correct += 1
        i += 1

    print("Accuracy: " + str(100 * correct/i) + "%")

#############################################################################################################################
#############################################################################################################################

PUNCTUATION = [".", "-", "_", ",", "?", "!", "'", "\"", "\`", "*", "@", "#", "$", "%", "^", "&", "(", ")", "/", "\\", "\+"]
stopwords_file = open("stopwords.txt", "r")
STOP_WORDS = stopwords_file.read().splitlines()
DEFAULT_PROBABILITY = 0.0001
WORD_WEIGHT = 100000

def topicModelClassifyMovie(inputOverview): 
    train_genre_overviews_df, overview_train, overview_test, genre_train, genre_test = getTrainTestSplitAsDFFromDF("movie_data.csv")
    train_genre_overviews_df = retrieveCleanedData(train_genre_overviews_df)
    unique_genres, genre_index_map, unique_words, word_index_map, topic_model = generateTopicModel(train_genre_overviews_df)
    movie_genre = classifyMovieOverview(inputOverview, unique_genres, genre_index_map, unique_words, topic_model)
    return movie_genre[0]