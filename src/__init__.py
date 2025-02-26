from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import pickle

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": ["http://192.168.21.215:81"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

model = 'src/models/xgb_models.pkl'

with open(model, 'rb') as file:
    model = pickle.load(file)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"]
)

from src import routes, routes_master_data, models
