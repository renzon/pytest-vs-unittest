from unittest import TestCase


class MultiParamTestCase(TestCase):
    def test_multi_param_stuff(self):
        for i in range(10):
            with self.subTest(i):
                self.assertEqual(0, i)