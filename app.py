from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'visitors.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for Visitor
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)

# Check and initialize the database before first request (inside function)
def init_db():
    db.create_all()
    if Visitor.query.first() is None:
        # If no record exists, initialize with a visitor count of 0
        new_visitor = Visitor(count=0)
        db.session.add(new_visitor)
        db.session.commit()

@app.route('/')
def home():
    init_db()  # Initialize DB if it hasn't been initialized yet
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    init_db()  # Ensure database exists and is initialized
    visitor = Visitor.query.first()
    visitor.count += 1
    db.session.commit()  # Save the updated count
    return render_template('portfolio.html', count=visitor.count)

if __name__ == '__main__':
    app.run(debug=True)
