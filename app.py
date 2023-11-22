from flask import Flask, request, jsonify
from pymongo import MongoClient 
from bson import json_util
import json

app = Flask(__name__) 

# Connect to MongoDB 
with open('config.json') as config_file:
    config_data = json.load(config_file)
    client = MongoClient(config_data['DB_URI']) 
    db = client[config_data['DB_NAME']]

@app.route("/")
def home():
    mycollection = db['users'] 
    document = mycollection.find_one({'username': "test"}) 
    return json.loads(json_util.dumps(document))