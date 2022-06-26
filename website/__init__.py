from flask import Flask
from flask_restful import Api


import logging


def create_app():

    app = Flask(__name__)
    api = Api(app)
    app.config['SECRET_KEY'] = "sdkdlkl3kjl"
    app.config.SESSION_COOKIE_SAMESITE = 'None'
    app.config.SESSION_COOKIE_SECURE = 'True'

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.StreamHandler()]
    )

    from .views import views
    from .api import Api_home, Greet, Info

    app.register_blueprint(views, url_prefix="/")
    api.add_resource(Info, '/api/info')
    api.add_resource(Api_home, '/api')
    api.add_resource(Greet, '/api/greet', '/api/greet/<string:name>')

    return app
