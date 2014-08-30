#!/usr/bin/env python
#-*- coding: utf-8 -*-

from selenium import webdriver
import time, lxml.html
ChromePath = r"/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/archive/2014_07_05_Flight/chromedriver"
browser = webdriver.Chrome(executable_path=ChromePath)


url = "https://gorod.mos.ru/?show=problem&zone=1&district=9"

def giveRegion(i):
	url = "https://gorod.mos.ru/?show=problem&zone=33&district=%d" %(i)

	def all_same(items):
		return all(x == items[0] for x in items)

	browser.get(url)
	

	dom = lxml.html.fromstring(browser.page_source)
	result = [ x.text.encode('utf-8') for x in dom.cssselect('span.remark')]
	# print len(result), '|', '|'.join(result)
	# print all_same(result)
	if len(result)>0 and all_same(result):
		zone, region = result[0].split('—')
		print "|".join([zone, region, str(i)])
	else:
		print "nope|%d|%s" % (i, url)
	time.sleep(10)



# giveRegion(3)

for i in xrange(1,190):
	giveRegion(i)

browser.close()