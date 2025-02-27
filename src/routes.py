from flask import request, jsonify, send_from_directory
from src import app, db
from src.services import recommend_products, encrypt_data
from src.models import UserInput, UserFirstChoice, MasterDataProducts, MasterDataSegmentation, SalaryRange, JobType
from sqlalchemy import or_
from flask_swagger_ui import get_swaggerui_blueprint
import os

@app.route('/')
def home():
    return "Hello, Flask in Docker!"

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"  # Path ke file JSON Swagger

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Flask API Documentation"},
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/static/swagger.json")
def swagger_json():
    return send_from_directory(os.path.dirname(__file__), "swagger.json")

@app.route('/recommendations', methods=['POST'])
def recommendations():
    try:
        input = request.get_json()

        age = input['age']
        salary_id = input['salary']  # Now receiving ID directly
        job_id = input['job']  # Now receiving ID directly
        gender = input['gender']
        province = input['province']

        # Fetch salary and job by ID instead of label
        salary_range = SalaryRange.query.get(salary_id)
        job_type = JobType.query.get(job_id)

        if not salary_range or not job_type:
            return jsonify({"error": "Invalid salary or job ID"}), 400

        encrypted_age = encrypt_data(str(age))
        encrypted_province = encrypt_data(province)

        # Get user segmentation
        segmentation = get_user_segmentation(age, salary_range.id, job_type.id)

        # Save user data using ID references
        new_user_input = UserInput(age=encrypted_age, salary=salary_range.id, job=job_type.id, gender=gender, province=encrypted_province, segmentation=segmentation['name'])
        db.session.add(new_user_input)
        db.session.commit()

        # Get recommended products
        result = recommend_products(age, salary_range.id, job_type.id)

        if segmentation['name'] == "Eksplorator Finansial":
            return jsonify({
                "user_input_id": new_user_input.id,
                "segmentation": ({
                    "name": "Eksplorator Finansial",
                    "desc": "Selalu ingin tahu dan berani mencoba berbagai peluang finansial untuk pertumbuhan yang maksimal."
                }),
                "products": [
                    {
                        "alias": "tabungan-wadiah",
                        "name": "Tabungan Wadiah",
                        "desc": "Menjaga Harta Anda Tetap Murni",
                        "image_uri": "https://i.postimg.cc/rs78t9Qw/tabungan-wadiah.jpg"
                    },
                    {
                        "alias": "tabungan-mudharabah",
                        "name": "Tabungan Mudharabah",
                        "desc": "Menjaga Harta Anda Tetap Murni",
                        "image_uri": "https://i.postimg.cc/pXnVMgLh/tabungan-mudharabah.jpg"
                    },
                    {
                        "alias": "ziswaf",
                        "name": "ZISWAF",
                        "desc": "Berbagi Lebih Mudah, Pahala Lebih Berkah",
                        "image_uri": "https://i.postimg.cc/4yydcyGB/ziswaf.jpg"
                    }
                ]
            }), 201

        return jsonify({
            "user_input_id": new_user_input.id,
            "segmentation": segmentation,
            "products": format_products(result)
        }), 201

    except KeyError as e:
        return jsonify({"error": "Missing field: " + str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/user-choices', methods=['POST'])
def user_choices():
    try:
        input = request.get_json()

        user_input_id = input["user_input_id"]
        choice = input["choice"]

        new_choice = UserFirstChoice(user_input_id=user_input_id, choice=choice)
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

    return [{"name": product.name, "alias": product.alias, "desc": product.desc, "image_uri": product.image_uri} for product in products]

def get_user_segmentation(age, salary_id, job_id):
    segment = MasterDataSegmentation.query.filter(
        or_(MasterDataSegmentation.min_age <= age, MasterDataSegmentation.min_age.is_(None)),
        or_(MasterDataSegmentation.max_age >= age, MasterDataSegmentation.max_age.is_(None)),
        or_(MasterDataSegmentation.salary_range_id == salary_id, MasterDataSegmentation.salary_range_id.is_(None)),
        or_(MasterDataSegmentation.job_type_id == job_id, MasterDataSegmentation.job_type_id.is_(None))
    ).first()

    return ({"name": segment.segment_name, "desc": segment.segment_desc}) if segment else ({"name": "Eksplorator Finansial", "desc": "Selalu ingin tahu dan berani mencoba berbagai peluang finansial untuk pertumbuhan yang maksimal."})
