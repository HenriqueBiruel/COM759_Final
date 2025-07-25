from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

mongodb_client = PyMongo(app, uri="mongodb+srv://user:pass@cluster0.2hoki.mongodb.net/Trabalho_final?retryWrites=true&w=majority&appName=Cluster0")
db = mongodb_client.db

from app import routes
