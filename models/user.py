from db import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'shipay_db'}  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('shipay_db.roles.id'), nullable=False)  
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date)

    
    user_claims = db.relationship('UserClaim', backref='user', lazy=True)
