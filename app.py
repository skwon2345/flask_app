from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
  
from flask_pymongo import PyMongo
from bson import ObjectId

# Instantiation
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreact'
mongo = PyMongo(app)

# Settings
CORS(app)

# Database
db = mongo.db.pythonreact


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def createUser():
  print(request.json)

  ret = {
    'name': request.json['name'],
    'email': request.json['email'],
    'password': request.json['password']
  }

  # id = db.insert({
  #   'name': request.json['name'],
  #   'email': request.json['email'],
  #   'password': request.json['password']
  # })

  # return jsonify(str(ObjectId(id)))
  return jsonify(ret)

@app.route('/users', methods=['GET'])
def getUsers():
  users = {
    'name': 'dfe',
    'email': 'sjfe@naver.com',
    'password': 'feafs'
  }
  # users = []
  # for doc in db.find():

  #     users.append({
  #         '_id': str(ObjectId(doc['_id'])),
  #         'name': doc['name'],
  #         'email': doc['email'],
  #         'password': doc['password']
  #     })
  return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
  user = db.find_one({'_id': ObjectId(id)})
  print(user)
  return jsonify({
      '_id': str(ObjectId(user['_id'])),
      'name': user['name'],
      'email': user['email'],
      'password': user['password']
  })

if __name__ == "__main__":
    app.run(debug=True)
