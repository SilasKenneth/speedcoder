from flask import Flask
from config import configurations


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config_name, "development"))
    return app