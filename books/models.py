from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    book_type = db.Column(db.Enum('1', '2', '3'), nullable=False)
    availability = db.Column(db.Boolean, default=True)
