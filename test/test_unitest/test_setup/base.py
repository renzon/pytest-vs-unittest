from unittest import TestCase

from setup_classes import Connection, Session


class SetupBaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = Connection()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def setUp(self):
        self.sess = Session()

    def tearDown(self):
        self.sess.close()