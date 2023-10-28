from os import listdir
from os.path import isfile, join
from digit_predictor import Model

model = Model()

def test_model():
    model = Model()

    # Test 1: Check if the model loads successfully
    assert hasattr(model, 'model'), "Model not loaded successfully"

    # Test 2: Check if predicting an invalid image path raises a ValueError
    try:
        invalid_img_path = 'invalid_path.png'
        model.predict_digit(invalid_img_path)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid image path did not raise ValueError")
    
    # Test 3: Check if predicting a non-image file raises a ValueError
    try:
        non_image_path = 'for_test.txt'
        model.predict_digit(non_image_path)
    except ValueError:
        pass
    else:
        raise AssertionError("Non-image file did not raise ValueError")

    # Test 4: Check if predicting a digit returns a valid result
    imgs = [f for f in listdir('img') if isfile(join('img', f))]
    
    try:
        for file_name in imgs:
            digit = int(file_name.split('.png')[0])
            prediction, confidence = model.predict_digit(join('img', file_name))
            
        assert type(prediction) == np.int64, "Type of predicted digit is not integer"
        assert 0 <= prediction <= 9, "Predicted digit is out of range"
        assert 0 <= confidence <= 1, "Confidence score is out of range"
        assert digit == prediction

    except Exception as e:
        raise AssertionError(f"Error in predict_digit: {e}")

test_model()