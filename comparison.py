#!/usr/bin/python
from screenshotlayer import screenshotlayer
import numpy as np
from PIL import Image
import requests
from io import BytesIO


def comparison(file1, file2):
    array1 = np.array(file1)
    print(f'array1: {array1}')
    array2 = np.array(file2)
    print(f'array2: {array2}')
    if array1.shape != array2.shape:
        return False
    # compare = np.array_equal(array1, array2)
    compare = np.setdiff1d(array1, array2)
    return compare


def file_compare(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    return comparison(image1, image2)


def arrays_matching(template="template.png"):
    template = template
    api_screenshot = requests.get(screenshotlayer(access_key, secret_keyword, url, params)).content
    compare_result = file_compare(template, BytesIO(api_screenshot))
    print(f'compare result: {compare_result}')
    return compare_result
    # threshold = 0.6
    # loc = np.where(compare_result >= threshold)
    # print(f'Loc: {loc}')
    # if loc[0].size > 0:
    #     print(f'Loc 0: {loc[0].size}')
    #     print("Template matched!")
    #     return True
    # else:
    #     print("Matching failed")


# set optional parameters (leave blank if unused)
params = {
    'fullpage': '',
    'width': '',
    'viewport': '',
    'format': 'PNG',
    'css_url': '',
    'delay': '5',
    'ttl': '300',
    'force': '',
    'placeholder': '',
    'user_agent': '',
    'accept_lang': '',
    'export': ''
}

# set your access key, secret keyword and target URL
access_key = "3f0042f8c12308b4dbd002dacf54d43c"
secret_keyword = "sky"
url = "https://adamautomation1.porannakawka.com"

print(arrays_matching())
