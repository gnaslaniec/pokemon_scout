import pytest
from app import create_app
from app.database import Base, engine, SessionLocal
from app.models import Pokemon


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    app = create_app()
    with app.test_client() as client:
        yield client
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(Pokemon).delete()
    session.commit()
    session.close()
