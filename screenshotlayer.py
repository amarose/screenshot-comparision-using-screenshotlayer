#!/usr/bin/python

import hashlib
import urllib.parse


def screenshotlayer(access_key, secret_keyword, url, args):
    # encode URL
    query = urllib.parse.urlencode(dict(url=url, **args))

    # generate md5 secret key
    secret_key = hashlib.md5(f'{url}{secret_keyword}'.encode('utf-8')).hexdigest()
    print(f"https://api.screenshotlayer.com/api/capture?access_key={access_key}&secret_key={secret_key}&{query}")

    return f"https://api.screenshotlayer.com/api/capture?access_key={access_key}&secret_key={secret_key}&{query}"
