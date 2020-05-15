#!/usr/bin/python

import hmac
import hashlib
import urllib.parse


def screenshotlayer(access_key, secret_keyword, url, args):
    # encode URL
    query = urllib.parse.urlencode(dict(url=url, **args))

    # generate md5 secret key
    secret_key = hashlib.md5(f'{url}{secret_keyword}'.encode('utf-8')).hexdigest()

    return f"https://api.screenshotlayer.com/api/capture?access_key={access_key}&secret_key={secret_key}&{query}"


# # set optional parameters (leave blank if unused)
# params = {
#     'fullpage': '',
#     'width': '',
#     'viewport': '',
#     'format': 'PNG',
#     'css_url': '',
#     'delay': '5',
#     'ttl': '300',
#     'force': '',
#     'placeholder': '',
#     'user_agent': '',
#     'accept_lang': '',
#     'export': ''
# }
#
# # set your access key, secret keyword and target URL
# access_key = "3f0042f8c12308b4dbd002dacf54d43c"
# secret_keyword = "sky"
# url = "https://adamautomation1.porannakawka.com"
#
# print(screenshotlayer(access_key, secret_keyword, url, params))
