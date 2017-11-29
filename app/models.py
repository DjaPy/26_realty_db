from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ads(db.Model):
    id = db.Column(db.Integer)
    settlement = db.Column(db.String(128))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(128))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    addresses = db.Column(db.String(128))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)