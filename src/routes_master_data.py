from flask import request, jsonify
from src import app, db
from src.models import MasterDataProducts, MasterDataProductsBenefits, Province

@app.route('/products', methods=['GET'])
def products():
    try:
        products = MasterDataProducts.query.all()
        products_list = [
            {
                "id": product.id,
                "alias": product.alias,
                "name": product.name,
                "desc": product.desc,
                "image_uri": product.image_uri
            }
            for product in products
        ]
        datas = {
            "message": "Product retrieve success",
            "status": "success",
            "datas": products_list
        }
        return jsonify(datas), 200
    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "Error",
            "datas": None
        })

@app.route('/products/<alias>', methods=['GET'])
def products_by_alias(alias):
    try:
        product = MasterDataProducts.query.filter_by(alias=alias).first()

        if not product:
            return jsonify({
                "message": "Product not found",
                "status": "error",
                "datas": None
            }), 404

        # Fetch benefits for the product
        benefits = MasterDataProductsBenefits.query.filter_by(master_data_product_id=product.id).all()

        product_data = {
            "id": product.id,
            "alias": product.alias,
            "name": product.name,
            "desc": product.desc,
            "image_uri": product.image_uri,
            "details": product.details,
            "benefits": [benefit.benefit for benefit in benefits]  # Extract benefit descriptions
        }

        response = {
            "message": "Product retrieve success",
            "status": "success",
            "datas": product_data
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "error",
            "datas": None
        }), 500

@app.route('/provinces', methods=['GET'])
def get_provinces():
    try:
        provinces = Province.query.all()
        province_list = [{"id": prov.id, "name": prov.name} for prov in provinces]

        return jsonify({
            "message": "Provinces retrieved successfully",
            "status": "success",
            "datas": province_list
        }), 200

    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "error",
            "datas": None
        }), 500
