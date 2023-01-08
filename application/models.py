from .database import db

class User(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)

class Post(db.Model):
    post_id = db.Column(db.String, autoincrement=True, primary_key=True)
    author = db.relationship("User", secondary='post_authors')
    body = db.Column(db.String, nullable=False)
    media = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime)

class Followers(db.Model):
    id = db.Column(db.String, autoincrement=True, primary_key=True)
    user_id = db.relationship("User", )
    