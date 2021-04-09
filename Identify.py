#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-04 11:13:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import re
from requests.packages import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup
import hashlib, sys
from colorama import init, Fore



init()
class Identify():

	def __init__(self, url, response, finger_library):
		self.url = url
		self.Cms_Name = ''
		self.response = response
		self.response.encoding = self.response.apparent_encoding
		self.head = ''
		for key in self.response.headers.keys():
			self.head = self.head + key + ':' + self.response.headers[key]
		# print(self.head)
		self.body = self.response.text
		# print(self.body)
		try:
			self.title = BeautifulSoup(self.body, 'lxml').findAll('title')[0].get_text()
		except IndexError:
			self.title = ''
		# print(type(self.title))
		self.finger_library = finger_library


	def index_identify(self, index_list, isTofile):
		for cms in index_list:
			if not isTofile:
				print(Fore.CYAN + '[Index] Testing {0} for {1}'.format(cms, self.url))
			for key in self.finger_library[cms]['index'].keys():
				if key == 'body':
					for pat in self.finger_library[cms]['index']['body']:
						if '&' in pat:
							pats = re.split('&', pat)
							if re.search(pats[0], self.body, re.I) and re.search(pats[1], self.body, re.I):
								self.Cms_Name = cms
								return
						elif re.search(pat, self.body, re.I):
							self.Cms_Name = cms
							return
				if key == 'title':
					for pat in self.finger_library[cms]['index']['title']:
						if re.search(pat, self.title, re.I):
							self.Cms_Name = cms
							return
				if key == 'head':
					for pat in self.finger_library[cms]['index']['head']:
						if '&' in pat:
							pats = re.split('&', pat)
							if re.search(pats[0], self.head, re.I) and re.search(pats[1], self.head, re.I):
								self.Cms_Name = cms
								return
						elif re.search(pat, self.head, re.I):
							self.Cms_Name = cms
							return


	def keyword_identify(self, keyword_list, headers, isTofile):
		for cms in keyword_list:
			if not isTofile:
				print(Fore.YELLOW + '[KeyWord] Testing {0} for {1}'.format(cms, self.url))
			for filename in self.finger_library[cms]['keyword'].keys():
				keyword_url = self.url + filename
				try:
					keyword_response = requests.get(keyword_url, headers=headers, timeout=2)
				except:
					continue
				keyword_response.encoding = keyword_response.apparent_encoding
				if keyword_response.status_code == 200:
					# print(self.finger_library[cms]['keyword'][filename])
					if self.finger_library[cms]['keyword'][filename].lower() in keyword_response.text.lower():
						self.Cms_Name = cms
						return 


	def md5_identify(self, md5_list, headers, isTofile):
		for cms in md5_list:
			if not isTofile:
				print(Fore.BLUE + '[MD5] Testing {0} for {1}'.format(cms, self.url))
			for filename in self.finger_library[cms]['md5'].keys():
				md5_url = self.url + filename
				try:
					md5_response = requests.get(md5_url, headers=headers, timeout=2)
				except:
					continue
				if md5_response.status_code == 200:
					m = hashlib.md5()
					m.update(md5_response.text.encode('utf-8'))
					md5 = m.hexdigest()
					m2 = hashlib.md5()
					m2.update(md5_response.content)
					md5_2 = m2.hexdigest()
					# print(md5, md5_2)
					if md5 == self.finger_library[cms]['md5'][filename] or md5_2 == self.finger_library[cms]['md5'][filename]:
						self.Cms_Name = cms
						return 