from users import app
from users.controllers import authController
from users.middlewares import middleware, AuthMiddleware


@app.route('/login', methods=['POST'])
def login():
    return authController.login()


@app.route('/register', methods=['POST'])
def register():
    return authController.register()


@app.route('/refresh', methods=['POST'])
@middleware(AuthMiddleware)
def refresh():
    return authController.refresh()


@app.route('/check', methods=['POST'])
@middleware(AuthMiddleware)
def check():
    return authController.check()
