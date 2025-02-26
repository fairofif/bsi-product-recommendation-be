from src import db
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import SMALLINT
from sqlalchemy import Text

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.String(255), nullable=False)
    salary = db.Column(SMALLINT(), nullable=False)
    job = db.Column(SMALLINT(), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    province = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=True)
    gender = db.Column(SMALLINT(), nullable=False)
    segmentation = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<User {self.id}, Age: {self.age}, Gender: {self.gender}>'

class UserFirstChoice(db.Model):
    __tablename__ = 'user_first_choice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    choice = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=True)

    user = db.relationship('User', backref=db.backref('choices', lazy=True))

    def __repr__(self):
        return f'<UserFirstChoice {self.id}, UserID: {self.user_id}, Choice: {self.choice}>'

class MasterDataProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alias = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    image_uri = db.Column(db.String(200), nullable=True)
    details = db.Column(db.Text, nullable=True)

    benefits = db.relationship('MasterDataProductsBenefits', backref='product', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<MasterDataProducts {self.id}, alias: {self.alias}, name: {self.name}>'


class MasterDataProductsBenefits(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_data_product_id = db.Column(db.Integer, db.ForeignKey('master_data_products.id'), nullable=False)
    benefit = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<MasterDataProductsBenefits {self.id}, product_id: {self.master_data_product_id}>'

class MasterDataSegmentation(db.Model):
    __tablename__ = "master_data_segmentation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    segment_name = db.Column(db.String(50), nullable=False)
    min_age = db.Column(db.Integer, nullable=True)
    max_age = db.Column(db.Integer, nullable=True)

    salary_range_id = db.Column(db.Integer, db.ForeignKey('salary_range.id'), nullable=True)
    job_type_id = db.Column(db.Integer, db.ForeignKey('job_type.id'), nullable=True)

    salary_range = db.relationship('SalaryRange', backref='segmentations')
    job_type = db.relationship('JobType', backref='segmentations')

    def __repr__(self):
        return f"<MasterDataSegmentation {self.id}, Segment: {self.segment_name}>"

class SalaryRange(db.Model):
    __tablename__ = "salary_range"

    id = db.Column(db.Integer, primary_key=True)
    range_label = db.Column(db.String(20), nullable=False)

class JobType(db.Model):
    __tablename__ = "job_type"

    id = db.Column(db.Integer, primary_key=True)
    job_label = db.Column(db.String(20), nullable=False)

class Province(db.Model):
    __tablename__ = "province"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)