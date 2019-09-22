from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

message = Blueprint('message',__name__)

# 初始化数据库
db = SQLAlchemy()
def init_db(app):
    db.init_app(app)

# 导入
import App.message.view