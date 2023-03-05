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

response = requests.post("https://files.quoccabank.com/login", proxies=proxy, verify=False, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

print(response.text)