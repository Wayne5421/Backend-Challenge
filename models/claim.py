from db import db

class Claim(db.Model):
    __tablename__ = 'claims'
    __table_args__ = {'schema': 'shipay_db'}  

    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    
    users_claims = db.relationship('UserClaim', backref='claim', lazy=True)
