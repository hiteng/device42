# import unittest
# import mock_func
# from mock_func import Calculator
#
#
# class TestCalculator(unittest.TestCase):
#
#
#     def test_sum(self):
#         res = mock_func.Calculator()
#         self.assertEqual(res.sum(2, 4), 6)

import unittest
from unittest import TestCase
import mock_func
from mock_func import Calculator
from mock import patch, MagicMock

class TestCalculator(TestCase):

    @patch('mock_func.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(), 9)

if __name__ == '__main__':
    unittest.main()
