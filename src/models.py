from src import db
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.String(255), nullable=False)
    salary = db.Column(TINYINT(), nullable=False)
    job = db.Column(TINYINT(), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    province = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=True)
    gender = db.Column(TINYINT(), nullable=False)

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

