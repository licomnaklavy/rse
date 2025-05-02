import os
from db.database import Database
from flask_app.flask_app import Flask_app


if __name__ == "__main__":
    database = Database()

    app = Flask_app()
    app.app.run()
