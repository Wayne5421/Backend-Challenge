from db import db

class UserClaim(db.Model):
    __tablename__ = 'user_claims'
    __table_args__ = {'schema': 'shipay_db'}  

    user_id = db.Column(db.BigInteger, db.ForeignKey('shipay_db.users.id'), primary_key=True)  
    claim_id = db.Column(db.BigInteger, db.ForeignKey('shipay_db.claims.id'), primary_key=True)  
