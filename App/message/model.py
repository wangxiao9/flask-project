from datetime import datetime

from App.message import db

# 数据模型
class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime,default=datetime.now(),index=True)