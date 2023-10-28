from keras.models import load_model
import os
import cv2
from PIL import ImageGrab, Image
import numpy as np
import PIL
import imghdr
from os import listdir
from os.path import isfile, join

class Model():
    def __init__(self):
        self.model = load_model('mn1ist.h5')
        pass
        
    def read_img(self, img_path):
        if type(img_path) == str and os.path.isfile(img_path):
            if imghdr.what(img_path).lower() in ['png', 'jpg', 'jpeg']:
                return Image.open(img_path)
            else:
                print('File is not an image')
                raise ValueError
        else:
            print('Link is not a file')
            raise ValueError
            
    def preprocessing_image(self, img_path):
        """function to preprocess the image to"""
        image = cv2.imread(img_path)
        grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(grey.copy(), 75, 255, cv2.THRESH_BINARY_INV)
        # cv2.imshow('binarized image', thresh)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(type(contours[0]))
        # print(len(contours[0]))
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
        #cv2.imshow('Contours', image) 
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)        
            # Creating a rectangle around the digit in the original image (for displaying the digits fetched via contours)
            cv2.rectangle(image, (x,y), (x+w, y+h), color=(0, 255, 0), thickness=2)
            # Cropping out the digit from the image corresponding to the current contours in the for loop
            digit = thresh[y:y+h, x:x+w]        
            # Resizing that digit to (18, 18)
            resized_digit = cv2.resize(digit, (18,18))        
            # Padding the digit with 5 pixels of black color (zeros) in each side to finally produce the image of (28, 28)
            padded_digit = np.pad(resized_digit, ((5,5),(5,5)), "constant", constant_values=0)        
            # Adding the preprocessed digit to the list of preprocessed digits
            preprocessed_digit = (padded_digit)
        return preprocessed_digit

    def predict_digit(self, img_path):
        """function to predict the digit. 
        Argument of function is PIL Image"""
        if type(img_path) == str and os.path.isfile(img_path):
            if imghdr.what(img_path) != None:
                if imghdr.what(img_path).lower() in ['png', 'jpg', 'jpeg']:
                    preprocessed_image = self.preprocessing_image(img_path)
                else:
                    print('File is not an image')
                    raise ValueError
            else:
                print('File is not an image')
                raise ValueError
        else:
            print('Link is not a file')
            raise ValueError
    
        # print(type(preprocessed_image))
        # print(preprocessed_image.shape)
        img = preprocessed_image.reshape(1, 28, 28, 1)
        img = img/255.0
        #predicting the digit
        result = self.model.predict([img])[0]
        return np.argmax(result), max(result)


if __name__ == '__main__':
    test_model = Model()
    mypath = 'Dataset/'
    onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and imghdr.what(join(mypath, f)) != None)]
    onlyfiles = [f for f in onlyfiles if imghdr.what(join(mypath, f)).lower() in ['png', 'jpg', 'jpeg']]

    if len(onlyfiles) >= 2:
        num1 = test_model.predict_digit(join(mypath, onlyfiles[0]))
        num2 = test_model.predict_digit(join(mypath, onlyfiles[1]))
        print('Done!')
        print(num1, num2)
    else:
        print('Not enough images. At least 2')
        raise ValueError
