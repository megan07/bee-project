#!/usr/bin/env python

"""
Provides example code snippets for accessing Google's Geocoder API.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pprint import pprint
import urllib

import requests


BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"


def build_url(**kwargs):
    """
    Helpers function for building the base url for calling the Geocoder API.
    """
    encoded_params = urllib.urlencode(kwargs)
    encoded_string = "{}{}".format(BASE_URL, encoded_params)
    return encoded_string


def call_api(**kwargs):
    """
    Wrapper function for calling the Geocoder API.
    """
    url = build_url(**kwargs)
    error_message = None

    try:
        res = requests.post(url, timeout=5)
    except:
        out = []
    else:
        if res.status_code != 200:
            out = []
        else:
            out = res.json()['results']

    return out


if __name__ == '__main__':
    pprint(call_api(address="123 main st ames ia"))
