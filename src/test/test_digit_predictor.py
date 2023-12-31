import unittest
import numpy as np
from os import listdir
from os.path import isfile, join
import sys
sys.path.append('.')

from digit_predictor import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        
    def test_valid_predict_digit(self):
        self.assertTrue(hasattr(self.model, 'model'), "Model loaded unsuccessfully")
        
        imgs = [f for f in listdir('test/img') if isfile(join('test/img', f))]
        
        for file_name in imgs:
            with self.subTest(file_name=file_name):
                digit = int(file_name.split('.png')[0])
                prediction, confidence = self.model.predict_digit(join('test/img', file_name))
                
                self.assertIsInstance(prediction, np.int64, "Type of predicted digit is not integer")
                self.assertTrue(0 <= prediction <= 9, "Predicted digit is out of range")
                self.assertTrue(0 <= confidence <= 1, "Confidence score is out of range")
                self.assertEqual(digit, prediction)

    def test_invalid_predict_digit(self):
        with self.assertRaises(ValueError):
            invalid_img_path = 'invalid_path.png'
            self.model.predict_digit(invalid_img_path)
        with self.assertRaises(ValueError):
            non_image_path = 'test/for_test.txt'
            self.model.predict_digit(non_image_path)

    def test_invalid_preprocessing_image(self):
        with self.assertRaises(AttributeError):
            not_existing_path = 'invalid_path.png'
            self.model.preprocessing_image(not_existing_path)



    
