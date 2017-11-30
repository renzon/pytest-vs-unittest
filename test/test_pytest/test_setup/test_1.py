import pytest


def test_db_save(session):
    """Test db save"""
    print('######## running save')


def test_db_delete(session):
    """Test db deletion"""
    print('######## running delete')

@pytest.mark.non_db
def test_non_db():
    """Test non db"""
    print('######## non db test')
