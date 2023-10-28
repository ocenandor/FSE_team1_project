from os import listdir
from os.path import isfile, join
from .digit_predictor import Model

test_path = '../Desktop/Project/test/img'
imgs = [f for f in listdir(test_path) if isfile(join(test_path, f))]

test_model = Model()

for file_name in imgs:
    digit = int(file_name.split('.png')[0])
    prediciton = test_model.predict_digit(join(test_path, file_name))[0]
    
    assert digit == prediciton