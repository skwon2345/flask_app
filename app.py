from flask import Flask, render_template, jsonify, request
from datetime import datetime
from flask_cors import CORS

from bson import ObjectId

import db

# Instantiation
app = Flask(__name__)

# Settings
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def createUser():
  print(request.json)

  post = db.db.post.insert_one({
    'name': request.json['name'],
    'email': request.json['email'],
    'password': request.json['password']
  })
  _id = post.inserted_id

  return jsonify(str(ObjectId(_id)))

@app.route('/users', methods=['GET'])
def getUsers():
  users = []
  for doc in db.db.post.find():
      users.append({
          '_id': str(ObjectId(doc['_id'])),
          'name': doc['name'],
          'email': doc['email'],
          'password': doc['password']
      })
      
  return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
  user = db.db.find_one({'_id': ObjectId(id)})
  print(user)
  return jsonify({
      '_id': str(ObjectId(user['_id'])),
      'name': user['name'],
      'email': user['email'],
      'password': user['password']
  })

if __name__ == "__main__":
    app.run(debug=True)
