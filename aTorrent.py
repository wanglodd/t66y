#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup
import re
import sys
import timeit
import docopt
import json


#class aTorrentPageWithHorse(object):
#	"""
#	This class is used for a search page which running on t66y 1024 website.
#	"""
#    def __init__(self,pageNumber):
#		self.pageNumber = pageNumber
#       self.base_url = "http://t66y.com/thread0806.php?fid=15&search=&page={page}".format(page=pageNumber)


class aTorrent(object):
	"""
	The input will be a weburl, then this class will return a URL object
	which contain URL header and its torrent URL
	"""

	def __init__(self, urlAddress):
		self.url = urlAddress

	def __getObject(self):
		try:
			r = requests.get(self.url, timeout=5)

			if not r.status_code // 100 == 2:
				return "Error: Unexpected response {}".format(r)

		except requests.exceptions.Timeout as e:
			return "Error, {}".format(e)
		except requests.exceptions.ConnectionError as e:
			return "Error, {}".format(e)
		return r

	def getHtml(self):
		"""
		Return string of torrent page
		"""
		self.text = self.__getObject().text
		return self.text

	def getTitle(self):
		"""
		Retun title of torrent page
		"""
		soup = BeautifulSoup(self.getHtml(), 'lxml', from_encoding='ISO-8859-1')
		self.title = soup.title
		return self.title.string

	def getHash(self):
		self.text = self.__getObject().text
		myHash = re.findall('http://www.rmdown.com/link.php\?hash=([0-9a-z]+)', self.text)
		return myHash

pn = aTorrent('http://t66y.com/htm_data/15/1512/1765207.html')

print(pn.url)
print(pn.getHtml())
print(pn.getTitle(),pn.getHash())
