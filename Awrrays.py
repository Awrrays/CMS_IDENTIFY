#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-05 15:10:56
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from lib import conf
from Identify import Identify
import threading
from colorama import init, Fore
import argparse, sys
from argparse import RawTextHelpFormatter


init()
print(Fore.CYAN, end='')
index_list, keyword_list, md5_list, finger_library = conf.identify_options()


'''
 *　　　　　　　　┏┓　　　┏┓+ +
 *　　　　　　　┏┛┻━━━┛┻┓ + +
 *　　　　　　　┃　　　　　　　┃ 　
 *　　　　　　　┃　　　━　　　┃ ++ + + +
 *　　　　　　 ████━████ ┃+
 *　　　　　　　┃　　　　　　　┃ +
 *　　　　　　　┃　　　┻　　　┃
 *　　　　　　　┃　　　　　　　┃ + +
 *　　　　　　　┗━┓　　　┏━┛
 *　　　　　　　　　┃　　　┃　　　　　　　　　　　
 *　　　　　　　　　┃　　　┃ + + + +
 *　　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
 *　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
 *　　　　　　　　　┃　　　┃
 *　　　　　　　　　┃　　　┃　　+　　　　　　　　　
 *　　　　　　　　　┃　 　　┗━━━┓ + +
 *　　　　　　　　　┃ 　　　　　　　┣┓
 *　　　　　　　　　┃ 　　　　　　　┏┛
 *　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
 *　　　　　　　　　　┃┫┫　┃┫┫
 *　　　　　　　　　　┗┻┛　┗┻┛+ + + +
'''


def simple_identify(url):
	headers = {'User-Agent':conf.random_ua()}
	response = conf.index_request(url, headers)
	i = Identify(url, response, finger_library)
	i.index_identify(index_list, isTofile)
	if lock.acquire(True):
		if i.Cms_Name:
			print(Fore.MAGENTA + '[Success] ' + url + ' : ' + i.Cms_Name)
			if isTofile:
				print(url, file=open('./result/' + i.Cms_Name + '.txt', 'a'))
		else:
			print(Fore.MAGENTA + '[Failed]  ' + url)
		lock.release()


def medium_identify(url):
	headers = {'User-Agent':conf.random_ua()}
	response = conf.index_request(url, headers)
	i = Identify(url, response, finger_library)
	i.index_identify(index_list, isTofile)
	if not i.Cms_Name:
		i.keyword_identify(keyword_list, headers, isTofile)
	if lock.acquire(True):
		if i.Cms_Name:
			print(Fore.MAGENTA + '[Success] ' + url + ' : ' + i.Cms_Name)
			if isTofile:
				print(url, file=open('./result/' + i.Cms_Name + '.txt', 'a'))
		else:
			print(Fore.MAGENTA + '[Failed]  ' + url)
		lock.release()
	

def detail_identify(url):
	headers = {'User-Agent':conf.random_ua()}
	response = conf.index_request(url, headers)
	i = Identify(url, response, finger_library)
	i.index_identify(index_list, isTofile)
	if not i.Cms_Name:
		i.keyword_identify(keyword_list, headers, isTofile)
		if not i.Cms_Name:
			i.md5_identify(md5_list, headers, isTofile)
	if lock.acquire(True):
		if i.Cms_Name:
			print(Fore.MAGENTA + '[Success] ' + url + ' : ' + i.Cms_Name)
			if isTofile:
				print(url, file=open('./result/' + i.Cms_Name + '.txt', 'a'))
		else:
			print(Fore.MAGENTA + '[Failed]  ' + url)
		lock.release()


if __name__ == '__main__':
	# url = 'http://www.Awrrays.cn'

	parser = argparse.ArgumentParser(description='CMS recognition tool.', usage=conf.usage)
	parser.add_argument('-u','--url', help='Single url recognition.')
	parser.add_argument('-f','--filename', help='For batch recognition, please enter the file name.')
	parser.add_argument('-t','--threadnum', default=15, help='Specify the number of threads, default=15')
	parser.add_argument('--level', default=1, choices=['1','2','3'], help='Level 1: index identify;  Level 2: keyword identify;  Level 3: md5 identify; default=1')
	args = parser.parse_args()

	url = args.url
	filename = args.filename
	level = args.level
	if level == '3':
		exefunc = detail_identify
	elif level == '2':
		exefunc = medium_identify
	else:
		exefunc = simple_identify
	threadnum = args.threadnum

	lock = threading.Lock()

	if url:
		print(conf.usage)
		print("[Start] This task is starting run. Please wait for a moment...")
		isTofile = 0
		exefunc(url)
		
	elif filename:
		print(conf.usage)
		print("[Start] This task is starting run. Please wait for a moment...")
		isTofile = 1
		threads = []

		for url in open(filename, 'r').readlines():
			t = threading.Thread(target=exefunc, args=(url.strip(), ))
			threads.append(t)

		for i in range(len(threads)):
			threads[i].start()
			while True:
				if len(threading.enumerate()) < threadnum:
					break
	else:
		parser.print_help()
		sys.exit()
