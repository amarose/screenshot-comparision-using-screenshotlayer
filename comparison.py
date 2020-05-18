#!/usr/bin/python
from screenshotlayer import screenshotlayer
import numpy as np
import requests
from io import BytesIO
import credentials
from PIL import Image
from scipy.linalg import norm


def array_to_grayscale(array):
    if len(array.shape) == 3:
        return np.average(array, -1)
    else:
        return array


def comparison(file1, file2):
    array1 = array_to_grayscale(np.array(file1))
    array2 = array_to_grayscale(np.array(file2))
    diff = array1 - array2
    mse = np.mean(diff**2)
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return m_norm/array1.size, z_norm/array1.size, mse


def file_compare(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    return comparison(image1, image2)


def arrays_matching(template="template.png"):
    api_screenshot = requests.get(screenshotlayer(access_key, secret_keyword, url, params)).content
    compare_result = file_compare(BytesIO(api_screenshot), template)
    return compare_result


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
access_key = credentials.access_key_keeper()
secret_keyword = credentials.secret_keyword_keeper()
url = credentials.url_keeper()

print(arrays_matching())
