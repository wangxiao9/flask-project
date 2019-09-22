from flask import render_template

from . import message


@message.route('/index')
def sayhello():
    return 'sayhello'

@message.route('/403/')
def page_not_found_test():
    return render_template('index.html')