from db import db

class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'shipay_db'}  

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    
    users = db.relationship('User', backref='role', lazy=True)
