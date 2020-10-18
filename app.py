from flask import Flask, render_template, jsonify, request
from datetime import datetime
from flask_cors import CORS
import os

from bson import ObjectId

#database 
import firebase_admin
from firebase_admin import credentials, firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Administrator\Desktop\stock\stocktrading-14119-2c743d2f58b4.json" # r converts normal string to raw string. (raw string is necessary for file path) 

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'stocktrading-14119',
})

db = firestore.client()

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
    try:
        doc_ref_overall = db.collection(u'test11').document('fe')
        doc_ref_overall.set(request.json)
        print("efe")

        return jsonify({"success":True}), 200
    except Exception as e:
        print("fesf")
        print(e)
        return f"An Error Occured: {e}"
        
                    

##  post = db.db.post.insert_one({
##    'name': request.json['name'],
##    'email': request.json['email'],
##    'password': request.json['password']
##  })
##  _id = post.inserted_id
##
##  return jsonify(str(ObjectId(_id)))

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        todo = db.collection(u'test11').document('fe').get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return f"An Error Occured; {e}"
    
##  users = []
##  for doc in db.db.post.find():
##      users.append({
##          '_id': str(ObjectId(doc['_id'])),
##          'name': doc['name'],
##          'email': doc['email'],
##          'password': doc['password']
##      })
##      
##  return jsonify(users)

##@app.route('/users/<id>', methods=['GET'])
##def getUser(id):
##  user = db.db.find_one({'_id': ObjectId(id)})
##  print(user)
##  return jsonify({
##      '_id': str(ObjectId(user['_id'])),
##      'name': user['name'],
##      'email': user['email'],
##      'password': user['password']
##  })

if __name__ == "__main__":
    app.run(debug=True)
