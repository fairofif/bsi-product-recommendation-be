from src import app, db
from src.db_init_data import clear_master_data, init_job_salary, init_product_benefits, init_products, init_provinces, init_segmentation
from src.models import UserInput, UserFirstChoice
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import os

def init_db_create():
    engine = create_engine(os.getenv("DATABASE_URL_TEST"))
    with engine.connect() as conn:
        conn.execute(text("COMMIT"))
        try:
            conn.execute(text("CREATE DATABASE test_bsi;"))
        except Exception as e:
            print(f"Database mungkin sudah ada: {e}")

def init_test_db():
    with app.app_context():
        init_test_db_jobs()

def init_test_db_jobs():
    db.create_all()
    clear_master_data()
    init_job_salary()
    init_products()
    init_product_benefits()
    init_segmentation()
    init_provinces()

def clear_unittest_records(unit_input_id):
    with app.app_context():
        try:
            db.session.query(UserFirstChoice).filter_by(unit_input_id=unit_input_id).delete()
            db.session.query(UserInput).filter_by(id=unit_input_id).delete()
            db.session.commit()
            print(f"Test records with unit_input_id {unit_input_id} deleted successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting test records: {e}")

def is_alias_present(items, alias_to_find):
    return any(item.get("alias") == alias_to_find for item in items)
