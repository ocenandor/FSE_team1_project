import unittest
import numpy as np
from os import listdir
from os.path import isfile, join
import sys
sys.path.append('.')

from digit_predictor import Model

class TestTriRight(unittest.TestCase):
    def test_valid(self):
        pass

    def test_invalid(self):
        model = Model()
        with self.assertRaises(ValueError):
            invalid_img_path = 'invalid_path.png'
            model.predict_digit(invalid_img_path)

    