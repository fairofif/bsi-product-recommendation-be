from flask import Flask
from src import app

@app.route('/')
def home():
    return "Hello, Flask in Docker!"

@app.route('/about')
def about():
    return "This is the About page"
