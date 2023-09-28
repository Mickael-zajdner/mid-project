from loans.routes import loans_bp
from customers.routes import customers_bp
from books.routes import books_bp
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from books.models import Book  # Import the Book model
from customers.models import Customer  # Import the Customer model
from loans.models import Loan  # Import the Loan model

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Register Blueprints

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(loans_bp, url_prefix='/loans')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
