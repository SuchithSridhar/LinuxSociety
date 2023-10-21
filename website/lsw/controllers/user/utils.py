import hashlib
import base64
from ... import models


def hash_password(password: str):
    hasher = hashlib.sha512()
    hasher.update(password.encode())
    return base64.urlsafe_b64encode(hasher.digest()).decode('UTF-8')


def authenticate_user(email: str, password: str) -> models.User:
    password_hash = hash_password(password)
    user = models.User.query.filter_by(email=email).first()

    if user is None:
        return None

    if (user.password == password_hash or
            user.password == password):
        return user

    return None
