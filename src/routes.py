from flask import request, jsonify
from src import app, db
from src.services import recommend_products
from src.models import User

@app.route('/')
def home():
    return "Hello, Flask in Docker!"

@app.route('/about')
def about():
    return "This is the About page"

@app.route('/recommendations', methods=['POST'])
def recommendations():
    try:
        input = request.get_json()

        age = input['age']
        salary = input['salary']
        job = input['job']
        gender = input['gender']
        province = input['province']

        new_user = User(age=age, salary=salary, job=job, gender=gender, province=province)
        db.session.add(new_user)
        db.session.commit()

        result = recommend_products(age, salary, job)

        return jsonify({
            "user_id": new_user.id,
            "products": result
        }), 201
    except KeyError as e:
        return jsonify({"Error": "Missing field"}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


    
