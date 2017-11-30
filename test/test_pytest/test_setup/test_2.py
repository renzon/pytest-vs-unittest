import pytest

pytestmark = pytest.mark.usefixtures('session')


def test_db_save():
    """Test db save"""
    print('######## running save 2')


def test_db_delete():
    """Test db deletion"""
    print('######## running delete 2')
