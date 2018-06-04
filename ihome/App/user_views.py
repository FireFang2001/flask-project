import os
import re

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from App.models import db, User
from utils import status_code
from utils.settings import UPLOAD_DIRS
from utils.functions import is_login

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('index.html')


@user_bp.route('/createtable/')
def create_table():
    db.create_all()
    return '创建成功'


# 注册页面
@user_bp.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


# 注册api
@user_bp.route('/register/', methods=['POST'])
def user_register():
    register_dict = request.form
    mobile = register_dict.get('mobile')
    password = register_dict.get('password')
    password2 = register_dict.get('password2')

    if not all([mobile, password, password2]):
        return jsonify(status_code.USER_REGISTER_PARAMS_ERROR)

    if not re.match(r'^1[345789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    if User.query.filter(User.phone == mobile).count():
        return jsonify(status_code.USER_REGISTER_MOBILE_IS_EXIST)

    if password != password2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_ERROR)

    user = User()
    user.phone = mobile
    user.name = mobile
    user.password = password
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 登录页面
@user_bp.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


# POST登录api
@user_bp.route('/login/', methods=['POST'])
def user_login():
    user_dict = request.form

    mobile = user_dict.get('mobile')
    password = user_dict.get('password')

    if not all([mobile, password]):
        return jsonify(status_code.PARAMS_ERROR)

    if not re.match(r'^1[345789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    user = User.query.filter(User.phone == mobile).first()
    if user:
        if user.check_pwd(password):
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PASSWORD_ERROR)
    else:
        return jsonify(status_code.USER_LOGIN_NOT_EXIST)


@user_bp.route('/my/')
@is_login
def my():
    return render_template('my.html')


# 获取用户信息api
@user_bp.route('/user/', methods=['GET'])
@is_login
def get_user_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    return jsonify(user=user.to_basic_dict(), code=200)


@user_bp.route('/profile/', methods=['GET'])
@is_login
def user_profile():
    return render_template('profile.html')


# 修改用户信息接口
@user_bp.route('/user/', methods=['PUT'])
@is_login
def modify_user_profile():
    user_dict = request.form
    file_dict = request.files

    if 'name' in user_dict:
        name = user_dict['name']
        if User.query.filter(User.name == name).first():
            return jsonify(status_code.USER_NAME_EXIST)
        else:
            user = User.query.filter(User.id == session['user_id']).first()
            user.name = name
            try:
                user.add_update()
                return jsonify(code=status_code.OK, name=name)
            except Exception as e:
                return jsonify(status_code.DATABASE_ERROR)

    if 'avatar' in file_dict:
        f1 = file_dict['avatar']

        if not re.match(r'^image/.*$', f1.mimetype):
            return jsonify(status_code.USER_UPLOAD_IMAGE_ERROR)

        url = os.path.join(UPLOAD_DIRS, f1.filename)
        f1.save(url)
        user = User.query.filter(User.id == session['user_id']).first()
        image_url = os.path.join('/static/upload/', f1.filename)
        user.avatar = image_url
        try:
            user.add_update()
            return jsonify(code=status_code.OK, url=image_url)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)


@user_bp.route('/auth/')
@is_login
def id_auth():
    return render_template('auth.html')


# 获取实名认证信息api
@user_bp.route('/auths/', methods=['GET'])
@is_login
def get_user_auth():
    user = User.query.get(session['user_id'])
    if user.id_card and user.id_name:
        return jsonify(code=status_code.OK,
                       id_name=user.id_name,
                       id_card=user.id_card)
    else:
        return jsonify(code=0)


# 实名认证api
@user_bp.route('/auths/', methods=['POST'])
@is_login
def user_auth():
    user_dict = request.form
    real_name = user_dict.get('real_name')
    id_num = user_dict.get('id_num')

    if not all([real_name, id_num]):
        return jsonify(status_code.PARAMS_ERROR)

    if not re.match(r'\d{18}$', id_num):
        return jsonify(status_code.USER_ID_NUMBER_ERROR)

    if User.query.filter(User.id_card == id_num).first():
        return jsonify(status_code.USER_ID_NUMBER_EXIST)
    else:
        user = User.query.filter(User.id == session['user_id']).first()
        user.id_name = real_name
        user.id_card = id_num
        try:
            user.add_update()
            return jsonify(code=status_code.OK)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)


@user_bp.route('/logout/')
@is_login
def user_logout():
    session.clear()
    return jsonify(status_code.SUCCESS)
