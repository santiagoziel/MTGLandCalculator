from flask import Flask
from flask_socketio import SocketIO
import redis
from dta_pkt.initDatabase import setinit
app = Flask(__name__)

socketio = SocketIO(app)

app.config['SECRET_KEY'] = "fortheloveofgodchangethis"
app.config["UPLOAD_FOLDER"] = "dta_pkt/decks/"

# r = redis.Redis(host="localhost", port=6379, db=0)
r = redis.Redis(host="db", port=6379, db=0)
if r.get("test") is None:
    setinit(r)
from dta_pkt import routes, socket_events
