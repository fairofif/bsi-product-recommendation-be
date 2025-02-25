from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
import pickle

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": ["http://localhost:5173"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

model = 'src/models/xgb_models.pkl'

with open(model, 'rb') as file:
    model = pickle.load(file)

from src import routes, models
