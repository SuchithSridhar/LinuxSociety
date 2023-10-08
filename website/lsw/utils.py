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
    def get_pre_render_data(flask, lang="en"):
        stream = open(f'suchiblog/config/locales/{lang}.yml')
        lang = yaml.load(stream, Loader=yaml.Loader)
        if flask is None:
            mode = 'light'
        else:
            mode = f'{flask.session.get("value")}'

        data = {
            'ln': lang,
            'mode': mode
        }
        return data
