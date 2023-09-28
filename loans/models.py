from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Loan(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    custID = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    bookID = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
