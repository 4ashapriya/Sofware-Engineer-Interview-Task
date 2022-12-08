from app import db
from sqlalchemy import ForeignKey
from app.user.models import User


# Database ORMs
class Test(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    v2 = db.Column(db.Integer)
    v5 = db.Column(db.Integer)
    v6 = db.Column(db.Integer)
    driving_style = db.Column(db.Integer)
    public_id = db.Column(ForeignKey(User.public_id))
