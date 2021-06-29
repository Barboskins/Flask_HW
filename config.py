import os
from dotenv import load_dotenv

db_name = os.getenv("DB_NAME", "flask_hw")
db_user = os.getenv("DB_USER", "owner_user")
db_password = os.getenv("DB_PASSWORD", "owner_password")

class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_password}@localhost:5432/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

