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
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append("..")
from tweetFX-logic.TwitterClient import TwitterClient
from models import User,LabelledTweets
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
api = Api(app)

CORS(app)

"""
    Search Twitter Service
    @seachTerm is the string a user is searching for
"""
@app.route("/twitterSeach/<searchTerm>")
def twitterSearch(searchTerm):
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
            return jsonify({'status': str(e)})

"""
Login allows users to login to the system
"""
@app.route("/login/<username>/<password>")
def login(username,password):
    #try except to handle error that may occur when loging into TweetFX
    try:
        # User allow us to search the database with the username and return the first reponse
        user = User.query.filter_by(username=username).first()
        #check if a user was return if not respond with invalid username
        #else if user password equals password in databe then return username for success
        # else return an mage to say an error occured with username or password.
        if user == None:
            return jsonify({'username':'invalid username'})
        elif(user.password==password):
            return jsonify({'username':username})
        else:
            return jsonify({'username':'invalid password or username'})
    except Exception as e:
        return jsonify({'error': str(e)})

"""
Save Labelled Tweets to Database
"""
@app.route("/saveTweetsToDB", methods=['GET', 'POST'])
def saveTweets():
    #error handling incase an error occurs 
    try:
        #check if the request was a POST http protocol
        if request.method == 'POST':
            # for loop through a list of labelled tweets
            for i in request.json:
                #Create a single Labelled Tweet and commit it to the database.
                labelledTweet = LabelledTweets(tweet=i['text'], sentiment=i['sentiment'])
                db.session.add(labelledTweet)
                db.session.commit()
            return return jsonify({'status':'successful'})
    except Exception as e:
            return jsonify({'status': str(e)})

"""
Register allows users to login to the system
"""
@app.route("/register/<username>/<password>/<email>")
def Register(username,password,email):
    #try except to handle error that may occur when loging into TweetFX
    try:
        # User allow us to search the database with the username and return the first reponse
        usernameRegisted =User.query.filter_by(username=username).first()
        emailRegisted = User.query.filter_by(email=email).first();
        if(usernameRegisted== None and emailRegisted==None):
            user = User(username=username,password=password,email=email)
            return jsonify({'status':'successful'})
        elif(usernameRegisted!=None):
            return jsonify({'status':'user already registed'})
        elif(emailRegisted!=None):
           return jsonify({'status':'user already registed'}) 
    except Exception as e:
        return jsonify({'status': str(e)})