"""
@author: dvo
"""
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import pandas as pd
from keras.models import model_from_json
import sys
sys.path.append("..")
from tweetFX-logic.TwitterClient import TwitterClient
from tweetFX-logic.SaveData import SaveData

app = Flask(__name__)
api = Api(app)

CORS(app)

"""
    Saving Data
    The Microservice uses POST to recieve the data
    @request.data will hold all the labelled tweets
    Will use Save Data to save the labelled tweets to a csv file called TrainingData.csv
"""
@app.route("/savingData",methods=['POST'])
def savingData(searchTerm):
    # try except added  in case the saveData false to write the data to the file
    # We can send a descent error mesage to the front-end
    try:
        # if determine if the request method used was a 'POST'
        if request.method == 'POST':
            # creating an object of SaveData class        
            saveData = SaveData()
            # calling Save Data function writCSV with the data in the request
            saveData.writeCsv(request.data)
            # return a status to save it worked correctly
            return jsonify({'status':'OK'})
    except Exception as e:
        # if an error occurs and error message will be returned to the font end
        return jsonify({'error': str(e)})
    

"""
    Search Twitter Service
    @seachTerm is the string a user is searching for
"""
@app.route("/tweetsSearch/<searchTerm>")
def searchTwitter(searchTerm):
    # try except added  in case the microservice or the twitter api dies
    # We can send a descent error mesage to the front-end
    try:
        # Creating an object of TwitterClient Class
        # Saving the instanciated object in twitterClientAPI
        twitterClientAPI = TwitterClient();
        # Calling a function to get tweets
        tweets = twitterClientAPI.get_tweets(query = searchTerm)
        # All the tweets will be turn into a JSON then it get sent to the user who requested it.
        # JSON is a universal way to transport data when using REST API microservices.
        return jsonify(tweets)
    except Exception as e:
            return jsonify({'error': str(e)})


if __name__ == '__main__':
    """
    Server will run on port 5002
    """
    app.run(port=5002)