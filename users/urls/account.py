from users import app
from users.controllers import accountController
from users.middlewares import middleware, AuthMiddleware


@app.route('/profile', methods=['GET'])
@middleware(AuthMiddleware)
def profile():
    return accountController.profile()

# @app.route('/<id>/reset-password', methods=['PUT'])
# def update_password(id):
    # return userController.update_password(id)
