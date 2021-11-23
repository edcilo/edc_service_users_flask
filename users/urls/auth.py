from users import app
from users.controllers import authController


@app.route('/login', methods=['POST'])
def login():
    return authController.login()

@app.route('/register', methods=['POST'])
def register():
    return authController.register()

