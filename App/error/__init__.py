# @Time    : 2019/9/22 下午8:43
# @Author  : WANGXIAO
from flask import Blueprint

errors = Blueprint('errors',__name__)

import App.error.error
