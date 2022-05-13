import email
from app import db

class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    
    def __repr__(self):
        return f'<User {self.username}'