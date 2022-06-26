from typing import Optional
from flask_restful import Resource, abort
from .utils import server_info


class Api_home(Resource):
    def get(self):
        return {'hello': 'world'}


class Greet(Resource):
    def get(self, name: Optional[str] = None):
        if not name:
            return self._greet_for_none(), 200
        else:
            return self._greet_for_name(name)

    def _greet_for_none(self):
        return {'hello': 'KingKong'}

    def _greet_for_name(self, name: str):
        if name:
            return {'hello': name}
        else:
            abort(400, message="name do not exist")


class Info(Resource):
    def get(self):
        val = server_info()
        return val
