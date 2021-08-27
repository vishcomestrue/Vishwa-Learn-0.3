# IMPORT MODULES
# Modules for this task (numpy, opencv, os)
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


#ADD UTILITY FUNCTIONS HERE
# You can define any utility functions for your code.
# Please add proper comments to ensure that your code is
# readable and easy to understand.
##############################################################


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
    img_file_path = img_dir_path + 'Sample1' + '.png'
    print('============================================')
    shapes = scan_image(img_file_path)
    if type(shapes) is dict:
        print(shapes)
        print('\nOutput generated. Please verify.')
    else:
        print('\n[ERROR] scan_image function returned a ' +
              str(type(shapes)) + ' instead of a dictionary.\n')
        exit()
