from users import app
from users.controllers import adminController
from users.middlewares import middleware, AuthMiddleware


@app.route('/admin', methods=['GET'])
@middleware(AuthMiddleware)
def list():
    return adminController.list()


@app.route('/admin', methods=['POST'])
@middleware(AuthMiddleware)
def create():
    return adminController.create()


@app.route('/admin/trash', methods=['GET'])
@middleware(AuthMiddleware)
def trash():
    return adminController.trash()


@app.route('/admin', methods=['DELETE'])
@middleware(AuthMiddleware)
def multiple_soft_deletion():
    return adminController.multiple_soft_deletion()


@app.route('/admin/restore', methods=['POST'])
@middleware(AuthMiddleware)
def multiple_restore():
    return adminController.multiple_restore()


@app.route('/admin/hard', methods=['DELETE'])
@middleware(AuthMiddleware)
def multiple_deletion():
    return adminController.multiple_deletion()


@app.route('/admin/<id>')
@middleware(AuthMiddleware)
def detail(id):
    return adminController.detail(id)


@app.route('/admin/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
def update(id):
    return adminController.update(id)


@app.route('/admin/<id>/password', methods=['PUT'])
@middleware(AuthMiddleware)
def update_password(id):
    return adminController.update_password(id)


@app.route('/admin/<id>/activate', methods=['POST'])
@middleware(AuthMiddleware)
def activate(id):
    return adminController.activate(id)


@app.route('/admin/<id>/deactivate', methods=['POST'])
@middleware(AuthMiddleware)
def deactivate(id):
    return adminController.deactivate(id)


@app.route('/admin/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
def soft_delete(id):
    return adminController.soft_delete(id)


@app.route('/admin/<id>/restore', methods=['POST'])
@middleware(AuthMiddleware)
def restore(id):
    return adminController.restore(id)


@app.route('/admin/<id>/hard', methods=['DELETE'])
@middleware(AuthMiddleware)
def delete(id):
    return adminController.delete(id)

