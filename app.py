from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'SecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123*@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
