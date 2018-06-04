from flask import Flask

from App.user_views import user_bp
from App.house_views import house_bp
from App.order_views import order_bp
from App.views import index_bp
from utils.settings import STATIC_DIR, TEMPLATE_DIR
from utils.functions import init_ext


def create_app(config):
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
    app.register_blueprint(blueprint=user_bp, url_prefix='/user')
    app.register_blueprint(blueprint=house_bp, url_prefix='/house')
    app.register_blueprint(blueprint=order_bp, url_prefix='/order')
    app.register_blueprint(blueprint=index_bp, url_prefix='/index')
    app.config.from_object(config)

    init_ext(app)

    return app
