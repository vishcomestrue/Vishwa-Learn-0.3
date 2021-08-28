# IMPORT MODULES
# Modules for this task (numpy, opencv, os)
##############################################################
import cv2
import numpy as np
import os

from matplotlib import pyplot as plt

##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


# ADD UTILITY FUNCTIONS HERE
# You can define any utility functions for your code.
# Please add proper comments to ensure that your code is
# readable and easy to understand.
##############################################################

def get_contours(img, color):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for everyContour in contours:

        area = cv2.contourArea(everyContour)
        cv2.drawContours(img, everyContour, -1, (255, 255, 255), 1)

        perimeter = cv2.arcLength(everyContour, True)
        approx = cv2.approxPolyDP(everyContour, 0.02 * perimeter, True)

        x, y, width, height = cv2.boundingRect(approx)
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 255, 255), 2)

        if len(approx) == 3:
            print(f"Triangle with area of {area} and perimeter of {perimeter}")
            objectShape = 'Triangle'
        elif len(approx) == 4:
            print(f"Quadrilateral with area of {area} and perimeter of {perimeter}")
            objectShape = 'Quadrilateral'
        elif len(approx) == 5:
            print(f"Pentagon with area of {area} and perimeter of {perimeter}")
            objectShape = 'Pentagon'
        elif len(approx) == 6:
            print(f"Hexagon with area of {area} and perimeter of {perimeter}")
            objectShape = 'Hexagon'
        else:
            print(f"Circle of area {area} and perimeter of {perimeter}")
            objectShape = 'Circle'

        cv2.imshow('newimgcontour', img)
        cv2.waitKey(0)

        return {objectShape: [color, area, x+width // 2, y+height // 2]}


##############################################################


def scan_image(img_file_path):
    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image
    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image
    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes

    ##############	ADD YOUR CODE HERE	##############

    img = cv2.imread(img_file_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # SLICING THE IMAGES BASED ON COLOR
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Looking for blue
    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    # Looking for red
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    # Looking for green
    lower_green = np.array([230, 100, 100])
    upper_green = np.array([240, 255, 255])

    # Separating out blue
    maskblue_img = cv2.inRange(img_hsv, lower_green, upper_green)
    # cv2.imshow('result', maskblue_img)

    resultblue_img = cv2.bitwise_and(img, img, mask=maskblue_img)
    # blue_img = cv2.cvtColor(resultblue_img, cv2.COLOR_HSV2RGB)
    grayblue_img = cv2.cvtColor(resultblue_img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow('newgray', grayblue_img)

    blurblue_img = cv2.GaussianBlur(resultblue_img, (7, 7), 1)
    # cv2.imshow('blurblue', blurblue_img)

    canny = cv2.Canny(grayblue_img, 50, 50)
    # cv2.imshow('canny', canny)

    shapes = get_contours(canny, 'green')

    # Separating out red
    # maskred_img = cv2.inRange(img_hsv, lower_red, upper_red)
    # cv2.imshow('mask', maskred_img)
    # resultred_img = cv2.bitwise_and(img, img, mask=maskred_img)
    # grayred_img = cv2.cvtColor(resultred_img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow('newgray', grayred_img)
    # cannyred = cv2.Canny(grayred_img, 100, 200)
    # cv2.imshow('cannyred', cannyred)

    # Separating out green
    # maskgreen_img = cv2.inRange(img_hsv, lower_green, upper_green)
    # resultgreen_img = cv2.bitwise_and(img, img, mask=maskgreen_img)
    # cv2.imshow('result', resultgreen_img)

    cv2.waitKey(0)

    ##################################################

    return shapes


##################################################
if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in ' + curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'

    # path to 'Sample1.png' image file
    # change the path when running with a new image
    img_file_path = img_dir_path + 'Sample3' + '.png'
    print('============================================')
    shapes = scan_image(img_file_path)
    if type(shapes) is dict:
        print(shapes)
        print('\nOutput generated. Please verify.')
    else:
        print('\n[ERROR] scan_image function returned a ' +
              str(type(shapes)) + ' instead of a dictionary.\n')
        exit()
