from flask import jsonify
from users import app


@app.route('/')
def app_version():
    return jsonify({
        'data': {
            'name': app.config.get('APP_NAME'),
            'version': app.config.get('APP_VERSION'),
        },
        'code': 200
    }), 200
