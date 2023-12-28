# app.py

from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__)

    # Configuration settings can be loaded from a file
    if config_filename:
        app.config.from_pyfile(config_filename)

    # Additional app configuration and setup can be done here

    # Register blueprints, views, and other components
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
