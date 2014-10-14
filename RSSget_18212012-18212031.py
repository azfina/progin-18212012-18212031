#!/usr/bin/python

#II3160 - Pemrograman Integratif
#Importing The Latest 24 Hours RSS Feed
#Dilla Anindita / 18212012
#Azfina Putri Anindita / 18212031

#Importing external libraries
from xml.dom import minidom
import time
import sys
import urllib
import datetime

#Set URL of RSS Feed
url='http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml'

#Parsing parameter
xmldoc = minidom.parse(urllib.urlopen(url))
itemlist = xmldoc.getElementsByTagName('item')

#Printing headers
print
print
print "                            NEW YORK TIMES                                "	
print "                    THE LATEST NEWS IN 24 HOURS                           "
print "Created By: Dilla Anindita (18212012) and Azfina Putri Anindita (18212031)"
print "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "

#Sorting news by publication date
itemlist.sort(key = lambda x:time.strptime(x.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z'))

#Getting news iteratively
i=1
for s in itemlist :
	itemtitle = s.getElementsByTagName('title')[0]
	pubDate = s.getElementsByTagName('pubDate')[0]
	#Set publication time
	pubTime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(pubDate.childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z')))
	#Get system time
	nowTime = datetime.datetime.now()
	#Set the time difference
	diffTime = nowTime - pubTime
	diffTime = diffTime.seconds+diffTime.days*24*60*60
	if diffTime <= 86400:
		itemcontent = s.getElementsByTagName('guid')[0]
		print
		print str(i) + ' . ' + itemtitle.childNodes[0].nodeValue
		print 'Published on ' + pubDate.childNodes[0].nodeValue
		print ' (' + itemcontent.childNodes[0].nodeValue + ')'
		i = i+1

print
print		
print "                   Thank you for using this program                       "
print "Created By: Dilla Anindita (18212012) and Azfina Putri Anindita (18212031)"
print "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
