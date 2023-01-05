import unittest
max_integer = __import__('6-max_integer').max_integer
"""A unittest module that tests ``6-max_integer``"""


class TestMaxInteger(unittest.TestCase):
    """Represents test cases"""

    def test_ordered(self):
        """Tests ordered lists"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_firstListMax(self):
        """Tests when the first list is maximum"""

        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_unordered(self):
        """Tests unordered list"""

        self.assertEqual(max_integer([3, 1, 965, 2, 0]), 965)

    def test_nagativeNumber(self):
        """Tests when either a list is all negative numbers or negative
        number/s is mixed with positive numbers"""

        self.assertEqual(max_integer([5, 0, -3, 10, -10]), 10)
        self.assertEqual(max_integer([-2, -4.5, -10, -3.6, -1]), -1)

    def test_string(self):
        """Tests when a string is in a list"""

        with self.assertRaises(TypeError):
            self.assertNotEqual(max_integer([1, 3, "Hello", 7]), 7)

    def test_float(self):
        """Tests when all lists are float"""

        self.assertEqual(max_integer([2, 4, 6.7, 4.6, 1]), 6.7)
