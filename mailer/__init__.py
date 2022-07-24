# sacar vars de entorno para config la DB, config la api para el Email services y tener el ambiente config
import os
from webbrowser import get
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY = os.environ.get("SENDGRID_API_KEY"), # <- nombre de la var de entorno con el valor de la api key
        SECRET_KEY = os.os.environ.get("SECRET_KEY"),
        DATABASE_HOST = os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD = os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER = os.environ.get("FLASK_DATABASE_USER"),
        DATABASE = os.environ.get("FLASK_DATABASE"),
    )

    return app