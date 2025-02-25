from flask import Flask, jsonify
from src import app
from src.models import User

@app.route('/internal-logs/users', methods=['GET'])
def internalLogsUsers():
    users = User.query.all()
    response = {
        'users': [user.to_dict() for user in users]
    }
    print(response)