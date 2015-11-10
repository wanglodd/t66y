#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup
import re
import sys

lai = sys.argv[1]

URL = 'http://t66y.com/htm_data/15/1511/1713256.html'

def gethash(a):
	r = requests.get(a)
	hash = re.findall('hash=([0-9a-z]+)',r.text)
	b = set(hash)
	f_url = 'http://www.rmdown.com/link.php?hash=' + b.pop()
	print(f_url)
	return f_url
#	if r.status_code == 200:
#		soup = BeautifulSoup(r.text, "lxml")

gethash(lai)
