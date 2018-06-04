import os
import re

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from App.models import User, House, Area, Facility, HouseImage

from utils import status_code
from utils.functions import db, is_login
from utils.settings import UPLOAD_DIRS

house_bp = Blueprint('house', __name__)


@house_bp.route('/myhouse/', methods=['GET'])
def myhouse():
    return render_template('myhouse.html')


@house_bp.route('/auth_myhouse/', methods=['GEt'])
def auth_myhouse():
    user = User.query.get(session['user_id'])
    if user.id_card:
        houses = House.query.filter(House.user_id == user.id).order_by(House.id.desc())
        hlist_list = []
        for house in houses:
            hlist_list.append(house.to_dict())
        return jsonify(hlist_list=hlist_list, code=status_code.OK)
    else:
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@house_bp.route('/newhouse/', methods=['GET'])
def newhouse():
    return render_template('newhouse.html')


@house_bp.route('/area_facility/', methods=['GET'])
def area_facility():

    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    facilities = Facility.query.all()
    facility_list = [facility.to_dict() for facility in facilities]

    return jsonify(area_list=area_list, facility_list=facility_list)


@house_bp.route('/newhouse/', methods=['POST'])
def user_newhouse():
    house_dict = request.form
    title = house_dict.get('title')
    price = house_dict.get('price')
    area_id = house_dict.get('area_id')
    address = house_dict.get('address')
    room_count = house_dict.get('room_count')
    acreage = house_dict.get('acreage')
    unit = house_dict.get('unit')
    capacity = house_dict.get('capacity')
    beds = house_dict.get('beds')
    deposit = house_dict.get('deposit')
    min_days = house_dict.get('min_days')
    max_days = house_dict.get('max_days')
    facility_ids = house_dict.getlist('facility')

    house = House()
    house.user_id = session['user_id']
    house.title = title
    house.area_id = area_id
    house.address = address
    house.price = price
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days

    if facility_ids:
        fas = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        house.facilities = fas

    try:
        house.add_update()
        return jsonify(code=status_code.OK, house_id=house.id)
    except:
        return jsonify(status_code.DATABASE_ERROR)

    # for facility_id in facility_ids:
    #     facility = Facility.query.get(facility_id)
    #     house.facilities.append(facility)
    #     db.session.add(house)
    # try:
    #     house.add_update()
    #     return jsonify(code=status_code.OK, house_id=house.id)
    # except:
    #     return jsonify(status_code.DATABASE_ERROR)


@house_bp.route('/house_img/', methods=['POST'])
def house_imgs():
    house_dict = request.form
    house_file = request.files
    if 'house_image' in house_file:
        house_img = house_file.get('house_image')
        if not re.match(r'^image/.*$', house_img.mimetype):
            return jsonify(status_code.USER_UPLOAD_IMAGE_ERROR)
        url = os.path.join(UPLOAD_DIRS, house_img.filename)
        house_img.save(url)
        house_id = house_dict.get('house_id')
        image = HouseImage()
        image.url = os.path.join('/static/upload/', house_img.filename)
        image.house_id = house_id
        try:
            image.add_update()
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)
        house = House.query.get(house_id)
        if not house.index_image_url:
            house.index_image_url = image.url
        try:
            house.add_update()
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)
        return jsonify(code=status_code.OK, image_url=image.url)


@house_bp.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


@house_bp.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)
    facilities = house.facilities
    facility_dict_list = [facility.to_dict() for facility in facilities]
    bookings = 1

    if 'user_id' not in session:
        bookings = 0

    elif house.user_id == session['user_id']:
        bookings = 2

    return jsonify(house=house.to_full_dict(),
                   facilities=facility_dict_list,
                   code=status_code.OK,
                   booking=bookings)


@house_bp.route('/booking/', methods=['GET'])
@is_login
def booking():
    return render_template('booking.html')
