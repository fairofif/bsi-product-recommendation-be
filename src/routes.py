from flask import request, jsonify
from src import app, db
from src.services import recommend_products, encrypt_data
from src.models import User, UserFirstChoice, MasterDataProducts

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

        encrypted_age = encrypt_data(str(age))
        encrypted_province = encrypt_data(province)

        new_user = User(age=encrypted_age, salary=salary, job=job, gender=gender, province=encrypted_province)
        db.session.add(new_user)
        db.session.commit()

        result = recommend_products(age, salary, job)

        return jsonify({
            "user_id": new_user.id,
            "products": format_products(result)
        }), 201
    except KeyError as e:
        return jsonify({"Error": "Missing field"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/user-choices', methods=['POST'])
def user_choices():
    try:
        input = request.get_json()

        user_id = input["user_id"]
        choice = input["choice"]

        new_choice = UserFirstChoice(user_id=user_id, choice=choice)
        db.session.add(new_choice)
        db.session.commit()

        return jsonify({
            "message": "User choice successfully saved"
        }), 201
    except KeyError as e:
        return jsonify({"Error": "Missing field"}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


def format_products(product_names):

    products = MasterDataProducts.query.filter(MasterDataProducts.name.in_(product_names)).all()

    return [{"name": product.name, "alias": product.alias} for product in products]
