from src import app, db
from src.db_init_data import init_segmentation, init_products, init_job_salary, clear_master_data, init_product_benefits, init_provinces

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
    clear_master_data()
    init_job_salary()
    init_products()
    init_product_benefits()
    init_segmentation()
    init_provinces()


