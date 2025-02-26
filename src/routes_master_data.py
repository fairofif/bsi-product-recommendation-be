from flask import request, jsonify
from src import app, db
from src.models import MasterDataProducts

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

        product_data = {
            "id": product.id,
            "alias": product.alias,
            "name": product.name,
            "desc": product.desc,
            "image_uri": product.image_uri
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