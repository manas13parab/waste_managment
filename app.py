
from flask import Flask

from .extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'

# Initialize extensions
db.init_app(app)

@app.route('/')
def home():
    return "Home Page"

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    # When running directly, create tables and run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)