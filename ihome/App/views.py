
from flask import Blueprint, render_template, request, jsonify, session
from sqlalchemy import or_, and_

from App.models import User, House, Area, Order

from utils import status_code

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index.html')


@index_bp.route('/index/', methods=['GET'])
def index_detail():
    if 'user_id' in session:
        user_name = User.query.get(session['user_id']).name
    else:
        user_name = ''
    houses = House.query.order_by(House.id.desc()).all()[:5]
    house_list = [house.to_dict() for house in houses]
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]
    return jsonify(code=status_code.OK,
                   areas=area_list,
                   user_name=user_name,
                   house_list=house_list)


@index_bp.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')


@index_bp.route('/allsearch/', methods=['GET'])
def to_search():
    search_dict = request.args

    area_id = search_dict.get('aid')
    start_date = search_dict.get('sd')
    end_date = search_dict.get('ed')
    sort_key = search_dict.get('sk', 'new')

    houses = House.query.filter(House.area_id == area_id) if area_id else House.query.filter()
    # 对房屋进行处理

    orders1 = Order.query.filter(Order.begin_date >= start_date, Order.end_date <= end_date)
    orders2 = Order.query.filter(or_(and_(Order.end_date >= start_date, Order.begin_date <= start_date),
                                     and_(Order.end_date >= end_date, Order.begin_date <= end_date)))

    order_list1 = [order.house_id for order in orders1]
    order_list2 = [order.house_id for order in orders2]
    order_list = list(set(order_list1 + order_list2))
    house_ids = [order for order in order_list]
    houses = houses.filter(House.id.notin_(house_ids))

    if sort_key == 'new':
        houses = houses.order_by(House.create_time.desc())
    elif sort_key == 'booking':
        houses = houses.order_by(House.order_count.desc())
    elif sort_key == 'price-inc':
        houses = houses.order_by(House.price.asc())
    elif sort_key == 'price-des':
        houses = houses.order_by(House.price.desc())

    house_list = [house.to_full_dict() for house in houses]

    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    return jsonify(code=status_code.OK,
                   houses=house_list,
                   areas=area_list)
