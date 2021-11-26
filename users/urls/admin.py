from users import app
from users.controllers import adminController


@app.route('/admin')
def list():
    return adminController.list()


@app.route('/admin', methods=['POST'])
def create():
    return adminController.create()


@app.route('/admin/<id>')
def detail(id):
    return adminController.detail(id)


@app.route('/admin/<id>', methods=['PUT'])
def update(id):
    return adminController.update(id)


@app.route('/admin/<id>/password', methods=['PUT'])
def update_password(id):
    return adminController.update_password(id)


@app.route('/admin/<id>/activate', methods=['POST'])
def activate(id):
    return adminController.activate(id)


@app.route('/admin/<id>/deactivate', methods=['POST'])
def deactivate(id):
    return adminController.deactivate(id)


@app.route('/admin/<id>', methods=['DELETE'])
def soft_delete(id):
    return adminController.soft_delete(id)


@app.route('/admin/<id>/restore', methods=['POST'])
def restore(id):
    return adminController.restore(id)


@app.route('/admin/<id>/hard', methods=['DELETE'])
def delete(id):
    return adminController.delete(id)
