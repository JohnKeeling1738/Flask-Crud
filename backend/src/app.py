import json
from django.shortcuts import redirect
from flask import Flask, render_template, request, jsonify, url_for
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)

app.config["MONGO_URI"]='mongodb://localhost:27017/flask'
mongo = PyMongo(app)

CORS(app)

# @app.route("/")
# def index():
    
#     return '<h1>Hello World</h1>'


@app.route("/users",methods=["POST"])
def createUser():
    db =mongo.db.users
    name =request.json['name']
    email =request.json['email']
    contact = request.json['contact']
    address =request.json['address']
    db.insert_one({'name':name,'email':email,'contact':contact,'address':address})

    return jsonify({'msg':'User Added Successfully'})
            
@app.route('/users',methods=['GET'])
def getUsers():
    db = mongo.db.users
    helper =[]
    for i in db.find():
        helper.append({
            '_id':str(ObjectId(i['_id'])),
            'name':i['name'],
            'email':i['email'],
            'contact':i['contact'],
            'address':i['address'],})
    return jsonify(helper)

@app.route("/users/<id>",methods = ['GET'])
def getUser(id):        
    db = mongo.db.users
    user = db.find_one({'_id':ObjectId(id)})
    return jsonify({
        '_id':str(ObjectId(user['_id'])),
            'name':user['name'],
            'email':user['email'],
            'contact':user['contact'],
            'address':user['address']
    })

@app.route('/users/<id>',methods=['DELETE'])
def deleteUsers(id):
    db = mongo.db.users
    db.delete_one({'_id':ObjectId(id)})
    return jsonify({'msg':'User Deleted'})

@app.route('/users/<id>',methods=['PUT'])
def updateUsers(id):
    db = mongo.db.users
    db.update_one({'_id':ObjectId(id)},
    {'$set':{
        'name':request.json['name'],
        'email':request.json['email'],
        'contact':request.json['contact'],
        'address':request.json['address'],
    }})
    return jsonify({'message':"User Updated Successfully"})


if __name__ == '__main__':
    app.run(debug = True)