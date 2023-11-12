from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7bd2e4717f093d7f657b5c40e4e9eead'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# # Create the Flask application context
# app.app_context().push()

# # Create tables within the context
# db.create_all()

from flaskblog import routes
