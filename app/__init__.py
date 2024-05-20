from flask import Flask
from flask_socketio  import SocketIO
import os
from dotenv import load_dotenv
from .database import init_db
load_dotenv()  
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins=os.getenv('CLIENT_URL'))

# Registrar eventos
# from .socketio_events import *

