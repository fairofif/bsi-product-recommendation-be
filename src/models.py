from src import db
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import SMALLINT

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

    def __repr__(self):
        return f'<MasterDataProducts {self.id}, alias: {self.alias}, name: {self.name}>'
