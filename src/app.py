from pathlib import Path
from flask import Flask
from flask_cors import CORS
from routes import register_routes
from db import init_db
from common import SQLITE_DB_URI

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    Path(app.root_path, "instance").mkdir(exist_ok=True)
    
    
    if not app.config.from_pyfile("config.py", silent=True):
        app.config.from_mapping({
            "SERVER_NAME": "localhost:5000",
            "DEBUG": True,
            "SQLALCHEMY_DATABASE_URI": SQLITE_DB_URI,
            "SQLALCHEMY_ECHO": True
        })
    
    init_db(app)
    register_routes(app)
    
    return app
