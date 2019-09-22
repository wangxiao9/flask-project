from flask import Flask



# 初始化
from flask_bootstrap import Bootstrap

from App.error import errors
from App.message import message, init_db
from App.setting import envs


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(envs.get('develop_env'))
    app.register_blueprint(blueprint=message)
    app.register_blueprint(blueprint=errors)
    init_db(app)
    return app