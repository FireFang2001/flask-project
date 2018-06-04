import os
import re
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from App.models import User, House, Area, Facility, HouseImage, Order

from utils import status_code
from utils.functions import db
from utils.settings import UPLOAD_DIRS

order_bp = Blueprint('order', __name__)


@order_bp.route('/', methods=['POST'])
def post_order():
    order_dict = request.form
    house_id = order_dict.get('house_id')
    start_time = datetime.strptime(order_dict.get('start_time'), '%Y-%m-%d')
    end_time = datetime.strptime(order_dict.get('end_time'), '%Y-%m-%d')

    if not all([house_id, start_time, end_time]):
        return jsonify(status_code.PARAMS_ERROR)

    if start_time > end_time:
        return jsonify(status_code.ORDER_START_TIME_GT_END_TIME)

    house = House.query.get(house_id)
    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = start_time
    order.end_date = end_time
    order.house_price = house.price
    order.days = (end_time - start_time).days + 1
    order.amount = order.days * order.house_price
    try:
        order.add_update()
        return jsonify(code=status_code.OK)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


@order_bp.route('/order/', methods=['GET'])
def get_order():
    return render_template('orders.html')


@order_bp.route('/orders/', methods=['GET'])
def user_orders():
    user_id = session['user_id']
    orders = Order.query.filter(Order.user_id == user_id)
    order_dict_list = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, orders=order_dict_list)


@order_bp.route('/lorders/', methods=['GET'])
def lorders():
    return render_template('lorders.html')


@order_bp.route('/cus_orders/', methods=['GET'])
def cus_orders():
    # 第一种方法
    houses = House.query.filter(House.user_id == session['user_id'])
    houses_ids = [house.id for house in houses]
    orders = Order.query.filter(Order.house_id.in_(houses_ids)).order_by(Order.id.desc())
    order_list = [order.to_dict() for order in orders]
    # 第二种方法
    # houses = House.query.filter(House.user_id == session['user_id'])
    # order_list = []
    # for house in houses:
    #     orders = house.orders
    #     order_list.append(orders)
    # order_list = [order.to_dict() for order in order_list]

    return jsonify(orders=order_list, code=status_code.OK)


@order_bp.route('/order/<int:id>/', methods=['patch'])
def order_status(id):
    status = request.form.get('status')
    order = Order.query.get(id)
    order.status = status
    if status == 'REJECTED':
        comment = request.form.get('comment')
        order.comment = comment
    try:
        order.add_update()
        return jsonify(code=status_code.OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)
