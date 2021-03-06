from flask import jsonify
from users import app
from .auth import *
from .admin import *
from .account import *


@app.route('/about')
def app_version():
    return jsonify({
        'data': {
            'name': app.config.get('APP_NAME'),
            'version': app.config.get('APP_VERSION'),
        },
        'code': 200
    }), 200
