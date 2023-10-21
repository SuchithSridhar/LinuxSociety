import os


class Config:
    SECRET_KEY = os.environ.get('LSW_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
