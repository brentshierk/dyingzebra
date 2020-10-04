#imports
from flask import Flask, render_template, redirect,url_for,jsonify,request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#app config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/" ,methods=['GET','POST'])


@app.route('/ping', methods=['GET'])
def ping_pong():
    
    return jsonify('pong!!')


@app.route('/Books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]
    


if __name__ == '__main__':
    app.run()