from flask import Flask

# node init
app = Flask(__name__)

from app import views
from app.blockchain import Blockchain

# init
blockchain = Blockchain()