import numpy as np
from src import model
from cryptography.fernet import Fernet
import os

def recommend_products(age, salary, job):
    model_result = model

    product_probabilities = {}
    for product, m in model_result.items():
        probabilities = m.predict_proba(np.array([[age,salary,job]]))
        product_probabilities[product] = probabilities[0, 1]
    print(product_probabilities.items())
    recommended_products = [product for product, probability in product_probabilities.items() if probability >= 0.8]
    print(recommend_products)
    return recommended_products

def encrypt_data(data):
    key = os.getenv("ENCRYPTION_KEY")
    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data.encode())

    return encrypted_data

def decrypt_data(data):
    key = os.getenv("ENCRYPTION_KEY")
    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(data).decode()

    return decrypted_data