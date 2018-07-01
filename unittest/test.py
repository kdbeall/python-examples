import unittest

# See https://docs.python.org/3/library/unittest.html#module-unittest


class TestExampleMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1+1, 2)

    def test_floating_point(self):
        self.assertAlmostEqual(1.0, 1.01, delta=0.02)

    def test_regex(self):
        self.assertRegex("bark...bark", "bark.*bark")

if __name__ == '__main__':
    unittest.main()
