import pytest

from setup_classes import Session, Connection


@pytest.fixture
def session():
    s = Session()
    yield s
    s.close()


@pytest.fixture(scope='session', autouse=True)
def connection():
    conn = Connection()
    yield conn
    conn.close()
