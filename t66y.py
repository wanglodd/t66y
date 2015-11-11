#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup
import re
import sys

your_page = input('Please enter which page you would like to scan: ')


BASE_URL = 'http://t66y.com/thread0806.php?fid=15&search=&page='
URL = BASE_URL + your_page.rstrip()

def getpage(a):
	laoshi_list = []
	r = requests.get(a)
	html = re.findall('htm_data(/[0-9]+/[0-9]+/[0-9]+\.html)', r.text)
	for i in html:
		c = 'http://t66y.com/htm_data' + i
		laoshi_list.append(c)
#	print(laoshi_list)
	return laoshi_list


def gethash(a):
	for link in a:
		r = requests.get(link)
		hash = re.findall('hash=([0-9a-z]+)',r.text)
		b = set(hash)
		f_url = 'http://www.rmdown.com/link.php?hash=' + b.pop()
		print(f_url)
		return f_url


test = getpage(URL)
gethash(test)
