import cv2
import numpy as np
from screenshotlayer import screenshotlayer
import requests
import credentials
from PIL import Image
from io import BytesIO


def template_matching(picture="template.png"):
    template = cv2.imread(picture)
    api_screenshot = requests.get(screenshotlayer(access_key, secret_keyword, url, params)).content
    open_screenshot = Image.open(BytesIO(api_screenshot))
    screenshot_array = np.array(open_screenshot, dtype=np.uint8)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    screenshot_gray = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where(result >= threshold)
    if loc[0].size > 0:
        print("Template matched!")
        cv2.destroyAllWindows()
        return True
    else:
        print("Matching failed")
        return False


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

print(template_matching())
