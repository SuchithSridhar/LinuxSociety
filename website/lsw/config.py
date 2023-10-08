import os


class Config:
    SECRET_KEY = os.environ.get('LSW_SECERT_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/site.db'
