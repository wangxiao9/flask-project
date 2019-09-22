# @Time    : 2019/9/22 下午7:50
# @Author  : WANGXIAO

def get_db_url(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('port') or '3306'
    NAME = dbinfo.get('NAME') or 'demo'
    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'QWwdjnjcnjkerj4567623333ednjkfjklf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER': 'mysqlconnector',
        'USER': 'root',
        'PASSWORD': 'root_123_wx',
        'HOST': '49.235.145.63',
        'PORT': '3306',
        'NAME': 'flaskdemo'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

envs = {
    'develop_env' : DevelopConfig
}