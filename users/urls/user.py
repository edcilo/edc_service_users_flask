from users import app
from users.controllers import userController


@app.route('/')
def list():
    return userController.list()


@app.route('/', methods=['POST'])
def create():
    return userController.create()


@app.route('/<id>')
def detail(id):
    return userController.detail(id)


@app.route('/<id>', methods=['PUT'])
def update(id):
    return userController.update(id)


@app.route('/<id>/activate', methods=['POST'])
def activate(id):
    return userController.activate(id)


@app.route('/<id>/deactivate', methods=['POST'])
def deactivate(id):
    return userController.deactivate(id)


@app.route('/<id>', methods=['DELETE'])
def soft_delete(id):
    return userController.soft_delete(id)


@app.route('/<id>/restore', methods=['POST'])
def restore(id):
    return userController.restore(id)


@app.route('/<id>/hard', methods=['DELETE'])
def delete(id):
    return userController.delete(id)
