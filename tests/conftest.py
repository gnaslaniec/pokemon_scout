import os
import pytest

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app import create_app
from app.database import Base, engine


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    app = create_app(testing=True)

    with app.test_client() as client:
        yield client

    Base.metadata.drop_all(bind=engine)
