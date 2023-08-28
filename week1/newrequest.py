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
    "requestBox": "POST /calculator HTTP/1.1\nHost: kb.quoccabank.com\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\nReferer: http://haas.quoccabank.com/\nContent-Type: application/x-www-form-urlencoded\nOrigin: http://haas.quoccabank.com\nConnection: keep-alive\n\n"
}


r1 = requests.post("https://haas.quoccabank.com", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Host" : "haas.quoccabank.com",
   "Content-Type": "application/x-www-form-urlencoded"
   })
cookie = r1.text.split("\n")[6].split(" ")[1].split("=")[1][:-1]
numbers = r1.text.split("\n")[13].split(" ")[2][:-1].split("+")
value = int(numbers[0]) + int(numbers[1])

params = {
    "requestBox": "POST /calculator HTTP/1.1\nHost: kb.quoccabank.com\nCookie: session=" + cookie + 
    "\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n" + 
    "Accept-Language: en-US,en;q=0.5\n" + 
    "Content-Length: " + str(len("answer=" + str(value))) + "\n" +
    "Referer: http://haas.quoccabank.com/\nContent-Type: application/x-www-form-urlencoded\n" +
    "Origin: http://haas.quoccabank.com\nConnection: keep-alive\n\nanswer=" + str(value) + "\n"
}

for i in range(21):
    r = requests.post("https://haas.quoccabank.com", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Host" : "haas.quoccabank.com",
    "Content-Type": "application/x-www-form-urlencoded"
    })
    print(r.text)
    cookie = r.text.split("\n")[6].split(" ")[1].split("=")[1][:-1]
    numbers = r.text.split("\n")[13].split(" ")[2][:-1].split("+")
    value = int(numbers[0]) + int(numbers[1])
    params = {
        "requestBox": "POST /calculator HTTP/1.1\nHost: kb.quoccabank.com\nContent-Length: " + 
        str(len("answer=" + str(value))) + "\nCookie: session=" + cookie + 
        "\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n" + 
        "Accept-Language: en-US,en;q=0.5\nReferer: http://haas.quoccabank.com/\nContent-Type: " +
        "application/x-www-form-urlencoded\nOrigin: http://haas.quoccabank.com\nConnection: keep-alive\n\nanswer=" + str(value)
    }