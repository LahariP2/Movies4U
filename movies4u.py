from flask import Flask, render_template, request
from TopicModel import topicModelClassifyMovie
from SearchEngine import searchEngineRecommendMovies

app = Flask(__name__)

@app.route("/")
def movies4u():
    return render_template('index.html', genre = "")
    
@app.route("/", methods=['POST'])
def classifyOverviewOrSearchMovies(): 

    inputOverview = request.form['inputOverview']
    inputQuery = request.form['inputQuery']

    # User clicked Classify button
    if (inputOverview != "" and inputQuery == ""): 
        # Classify movie into genre
        return render_template('index.html', overview = inputOverview, genre = topicModelClassifyMovie(inputOverview), recommendations = ["", "", "", "", ""])

    # User clicked Search button
    if (inputOverview == "" and inputQuery != ""): 
        # Call search engine to get top 5 movie recommendations
        return render_template('index.html', query = inputQuery, recommendations = searchEngineRecommendMovies(inputQuery))

    # Default home page
    return render_template('index.html', recommendations = ["", "", "", "", ""])


