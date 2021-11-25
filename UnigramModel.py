import pandas as pd

original_movie_data = pd.read_csv("movie_data.csv")
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

PUNCTUATION = [".", ",", "?", "!", "'", "\"", "\`", "*", "@", "#", "$", "%", "^", "&", "(", ")", "/", "\\", "\+"]

for punc in PUNCTUATION: 
    movie_data.loc[:, "Overview"] = movie_data.loc[:, "Overview"].str.replace(punc, "") 

# Split genres → If a movie is classified under multiple genres, split the genres into their own rows with same overview
genre_overview = pd.DataFrame()
for index, row in movie_data.iterrows():
    genres = row["Genre"].split(", ")
    for genre in genres: 
        row["Genre"] = genre
        genre_overview = genre_overview.append(row, ignore_index = True)
