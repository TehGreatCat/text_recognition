
import cv2
import numpy as np
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


def get_string(path):
    try:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.fastNlMeansDenoising(img,None,10,7,21 )
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        # cv2.imshow("Output", img)
        cv2.imwrite("buff.jpg", img)
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    except Exception as e:
        print(e)
    return  pytesseract.image_to_string(Image.open(path), lang='eng+rus')


# print(get_string("ts.png"))
















# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'


# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Path of working folder on Disk
# src_path = "C:/Users/Dakelnut/Desktop/test/"








# def get_string(path):
#     # Read image with opencv
#     img = cv2.imread(path)
#
#     # Convert to gray
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Apply dilation and erosion to remove some noise
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#
#     # Write image after removed noise
#     # cv2.imwrite(src_path + "removed_noise.png", img)
#
#     #  Apply threshold to get image with only black and white
#     #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#
#     # Write the image after apply opencv to do some ...
#     # cv2.imwrite(src_path + "thres.png", img)
#
#     # Recognize text with tesseract for python
#     result = pytesseract.image_to_string(img)
#
#     # Remove template file
#     #os.remove(temp)
#
#     return result

# str = src_path + "2.png"
# print(str)
# print('--- Start recognize text from image ---')
# print(get_string(src_path + "2.png"))
#
# print("------ Done -------")