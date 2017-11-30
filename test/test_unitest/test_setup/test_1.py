import pytest

from test.test_unitest.test_setup.base import SetupBaseTestCase


class Setup1TestCase(SetupBaseTestCase):
    def test_db_save(self):
        """Test db save"""
        print('######## running save')

    def test_db_delete(self):
        """Test db deletion"""
        print('######## running delete')

    @pytest.mark.non_db
    def test_non_db(self):
        """Test non db"""
        print('######## non db test')
