from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = "Assignmet!"
socketio = SocketIO(app, logger=True, engineio_logger=True,
                    cors_allowed_origins="*")
CORS(app)
