# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LotteryDraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    draw1 = db.Column(db.Integer, nullable=False)
    draw2 = db.Column(db.Integer, nullable=False)
    draw3 = db.Column(db.Integer, nullable=False)
