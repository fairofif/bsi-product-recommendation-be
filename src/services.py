import numpy as np
from src import model

def recommend_products(age, salary, job):
    model_result = model

    product_probabilities = {}
    for product, m in model_result.items():
        probabilities = m.predict_proba(np.array([[age,salary,job]]))
        product_probabilities[product] = probabilities[0, 1]

    recommended_products = [product for product, probability in product_probabilities.items() if probability >= 0.8]

    return recommended_products