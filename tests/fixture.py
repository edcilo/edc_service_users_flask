import pytest
from users import app as users_app


@pytest.fixture
def app():
    with users_app.app_context():
        pass
    yield users_app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

