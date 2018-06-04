from flask import render_template
from flask_script import Manager

from utils.App import create_app
from utils.config import Config

app = create_app(Config)

manager = Manager(app=app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
