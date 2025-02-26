from flask import request, jsonify
from src import app, db
from src.services import recommend_products, encrypt_data
from src.models import User, UserFirstChoice, MasterDataProducts, MasterDataSegmentation, SalaryRange, JobType
from sqlalchemy import or_

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
        new_user = User(age=encrypted_age, salary=salary_range.id, job=job_type.id, gender=gender, province=encrypted_province, segmentation=segmentation)
        db.session.add(new_user)
        db.session.commit()

        # Get recommended products
        result = recommend_products(age, salary_range.id, job_type.id)

        if segmentation == "Eksplorator Finansial":
            return jsonify({
                "user_id": new_user.id,
                "segmentation": segmentation,
                "products": [
                    {
                        "alias": "tabungan-wadiah",
                        "name": "Tabungan Wadiah"
                    },
                    {
                        "alias": "tabungan-mudharabah",
                        "name": "Tabungan Mudharabah"
                    },
                    {
                        "alias": "zifwaf",
                        "name": "ZIFWAF"
                    }
                ]
            }), 201

        return jsonify({
            "user_id": new_user.id,
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

def get_user_segmentation(age, salary_id, job_id):
    segment = MasterDataSegmentation.query.filter(
        or_(MasterDataSegmentation.min_age <= age, MasterDataSegmentation.min_age.is_(None)),
        or_(MasterDataSegmentation.max_age >= age, MasterDataSegmentation.max_age.is_(None)),
        or_(MasterDataSegmentation.salary_range_id == salary_id, MasterDataSegmentation.salary_range_id.is_(None)),
        or_(MasterDataSegmentation.job_type_id == job_id, MasterDataSegmentation.job_type_id.is_(None))
    ).first()

    return segment.segment_name if segment else "Eksplorator Finansial"
