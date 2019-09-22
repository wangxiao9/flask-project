# @Time    : 2019/9/22 下午8:20
# @Author  : WANGXIAO
from flask import render_template

from . import errors

@errors.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@errors.route('/404/')
def page_not_found_test():
    return render_template('errors/404.html'), 404