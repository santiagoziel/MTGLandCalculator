from flask import Flask
from flask_socketio import SocketIO
import redis
app = Flask(__name__)

socketio = SocketIO(app)

app.config['SECRET_KEY'] = "fortheloveofgodchangethis"
app.config["UPLOAD_FOLDER"] = "dta_pkt/decks/"

r = redis.Redis(host="localhost", port=6379, db=0)

from dta_pkt import routes, socket_events
