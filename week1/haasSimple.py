#!/usr/bin/python3

# featherbear.cc/UNSW-COMP6443
# Proxied request template
# - Useful for sending requests through a proxy, like Burp Suite

import re
import urllib
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


visited = []


pattern = "COMP"

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

def crawl(links):

    for endpoint in links:
        if endpoint not in visited:
            params = {
                "requestBox": "GET " + endpoint + " HTTP/1.1\nHost: kb.quoccabank.com\n" +
                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n" + 
                "Accept-Language: en-US,en;q=0.5\n" + 
                "Referer: http://haas.quoccabank.com/\nContent-Type: application/x-www-form-urlencoded\n" +
                "Origin: http://haas.quoccabank.com\nConnection: keep-alive\n\n"
            }

            r2 = requests.post("https://haas.quoccabank.com", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
                "Host" : "haas.quoccabank.com",
            "Content-Type": "application/x-www-form-urlencoded"
            })

            if ("COMP" in r2.text):
                print(r2.text)

            s = BeautifulSoup(r2.content, 'html.parser')
            tags = s.find_all('a', href=True)

            t = [a['href'] for a in tags]
            
            visited.append(endpoint)
            crawl(t)







params = {
    "requestBox": "GET /deep HTTP/1.1\n" + 
    "Host: kb.quoccabank.com\n" +
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif," +
    "image/webp,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\n" +
    "Referer: http://haas.quoccabank.com/\nContent-Type: application/x-www-form-urlencoded\n" +
    "Origin: http://haas.quoccabank.com\nConnection: keep-alive\n\n"
}


r1 = requests.post("https://haas.quoccabank.com", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Host" : "haas.quoccabank.com",
   "Content-Type": "application/x-www-form-urlencoded"
   })


soup = BeautifulSoup(r1.content, 'html.parser')

a_tags = soup.find_all('a', href=True)

href_links = [a['href'] for a in a_tags]


crawl(href_links)
