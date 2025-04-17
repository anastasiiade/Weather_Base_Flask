from flask import Flask
from .routes import init_routes

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
init_routes(app)