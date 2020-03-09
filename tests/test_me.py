import unittest

import unittest_ga


class MyTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(unittest_ga.__version__, "0.1.0")

    def test_second(self):
        self.assertEqual(unittest_ga.__version__, "0.1.0")
