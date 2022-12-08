from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from configparser import SafeConfigParser


app = Flask(__name__)
CORS(app)
config = SafeConfigParser()
config.read("configurations/db_config.ini")
app.config["SQLALCHEMY_DATABASE_URI"] = config.get(
    "SQLITE_DB", "SQLALCHEMY_DATABASE_URI"
)
app.config["SECRET_KEY"] = config.get("SQLITE_DB", "SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.get(
    "SQLITE_DB", "SQLALCHEMY_TRACK_MODIFICATIONS"
)

db = SQLAlchemy(app)
