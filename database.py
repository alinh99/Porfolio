from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    proficiency = db.Column(db.Integer)