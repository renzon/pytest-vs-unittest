from test.test_unitest.test_setup.base import SetupBaseTestCase


class Setup2TestCase(SetupBaseTestCase):
    def test_db_save(self):
        """Test db save"""
        print('######## running save 2')

    def test_db_delete(self):
        """Test db deletion"""
        print('######## running delete 2')

    def test_non_db(self):
        """Test non db"""
        print('######## non db test 2')
