from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import redis
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "fortheloveofgodchangethis"
app.config["UPLOAD_FOLDER"] = "dta_pkt/decks/"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
r = redis.Redis(host="localhost", port=6379, db=0)

login_manager = LoginManager()
login_manager.init_app(app)


from dta_pkt import models, forms, routes
