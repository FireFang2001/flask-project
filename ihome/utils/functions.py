import functools

from flask import session, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_ext(app):

    db.init_app(app=app)


def get_database_uri(dbs):
    user = dbs.get('USER')
    password = dbs.get('PASSWORD')
    host = dbs.get('HOST')
    port = dbs.get('PORT')
    name = dbs.get('NAME')
    database = dbs.get('DB')
    driver = dbs.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(database, driver, user, password, host, port, name)


def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            # 验证用户是否登录
            if 'user_id' in session:
                return view_fun()
            else:
                return redirect('/user/login/')
        except:
            return redirect('/user/login/')
    return decorator
