import datetime
import hashlib
import base64
import uuid
import yaml


class Utils:

    @staticmethod
    def create_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def hash_password(password: str):
        hasher = hashlib.sha512()
        hasher.update(password.encode())
        return base64.urlsafe_b64encode(hasher.digest()).decode('UTF-8')

    @staticmethod
    def date_now():
        return datetime.datetime.now()

