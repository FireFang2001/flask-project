import os
from utils.functions import get_database_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

DATABESE = {
    'DB': 'mysql',
    'DRIVER': 'pymysql',
    'HOST': 'localhost',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': 'root',
    'NAME': 'ihome',
}

SQLALCHEMY_DATABASE_URI = get_database_uri(DATABESE)

UPLOAD_DIRS = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')
