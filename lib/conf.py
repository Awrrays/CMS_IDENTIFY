#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-04 10:38:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import random
import json, sys
from requests.packages import urllib3
urllib3.disable_warnings()
import requests, os
from colorama import init, Fore

init()


def identify_options():
	finger_library = json.load(open('./lib/CMS_FINGER.json', 'r'))

	index_identify = []
	keyword_identify = []
	md5_identify = []

	for cms_name in finger_library.keys():
		for identify_option in finger_library[cms_name].keys():
			if identify_option == 'index':
				index_identify.append(cms_name)
			if identify_option == 'keyword':
				keyword_identify.append(cms_name)
			if identify_option == 'md5':
				md5_identify.append(cms_name)
	return index_identify, keyword_identify, md5_identify, finger_library


def random_ua():
	userAgents = [
	    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
	    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
	    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
	    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
	    "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
	]

	return random.choice(userAgents)


def index_request(url, headers):
	try:
		response = requests.get(url, headers=headers, timeout=5, verify=False)
	except ConnectionError:
		print(Fore.RED + "[!] %s connect error..." % url)
		sys.exit()
	except TimeoutError:
		print(Fore.RED + '[!] %s request timout...' % url)
		sys.exit()
	except:
		print(Fore.RED + "[!] An unknown error occurred...")
		sys.exit()

	return response


usage = r'''
    _____ ___ _   _  ____ _____ ____  ____  ____  ___ _   _ _____ 
   |  ___|_ _| \ | |/ ___| ____|  _ \|  _ \|  _ \|_ _| \ | |_   _|
   | |_   | ||  \| | |  _|  _| | |_) | |_) | |_) || ||  \| | | |  
   |  _|  | || |\  | |_| | |___|  _ <|  __/|  _ < | || |\  | | |  
   |_|   |___|_| \_|\____|_____|_| \_\_|   |_| \_\___|_| \_| |_|  
                                                               
   							by: Awrrays.
'''
