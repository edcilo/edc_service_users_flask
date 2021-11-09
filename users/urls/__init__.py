from flask import jsonify
from users import app


@app.route('/')
def app_version():
    return jsonify({
        'data': {
            'name': 'app',
            'version': '1.0.0',
        },
        'code': 200
    }), 200
