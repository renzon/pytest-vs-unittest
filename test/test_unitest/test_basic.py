from unittest import TestCase


class BasicTestCase(TestCase):
    def test_basic_stuff(self):
        self.assertTrue(True)

    def test_list(self):
        self.assertEqual([1, 3, 4], [1, 3, 5, 6])

    def test_string(self):
        self.assertEqual('unitest', 'unittest')
