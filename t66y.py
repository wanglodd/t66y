#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup
import re
import sys
import timeit
import docopt
import json

your_page = input('Please enter which page you would like to scan: ')


BASE_URL = 'http://t66y.com/thread0806.php?fid=15&search=&page='
URL = BASE_URL + your_page.rstrip()


def getpage(a):
    laoshi_list = []
    r = requests.get(a)
    if r.status_code != 200:
        sys.exit(1)
        print('HTTP code return is not 200...')
        print('Exit...')
    else:
        html = re.findall('htm_data(/[0-9]+/[0-9]+/[0-9]+\.html)', r.text)
        for i in html:
            c = 'http://t66y.com/htm_data' + i
            laoshi_list.append(c)
        print(laoshi_list)
    return laoshi_list


def gethash(a):
    torrent_list = []
    for link in a:
        r = requests.get(link)
        if not re.search('hash=([0-9a-z]+)', r.text):
            hset = set(re.findall('hash=([0-9a-z]+)', r.text))
            soup = BeautifulSoup(r.text, 'lxml')
            title = str(soup.title.string)
            b = {}
            b['title'] = title
            b['hash_id'] = hset
            print(b)
            torrent_list.append(b)
        else:
            continue
    print(torrent_list)
    return torrent_list


#test = getpage(URL)
#gethash(test)
