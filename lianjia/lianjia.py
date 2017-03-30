import urllib2
from bs4 import BeautifulSoup

# pgNum = 1
# url = 'http://bj.lianjia.com/ershoufang/xueyuanlu1/pg' + pageNum
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# soup = BeautifulSoup(response, 'lxml')

# priceList = soup.select('.totalPrice')

# print len(priceList)

# for i in priceList:
# 	print i.span.string

priceList = []

for i in range(1,4):
	url = 'http://bj.lianjia.com/ershoufang/xueyuanlu1/pg' + str(i)
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	soup = BeautifulSoup(response, 'lxml')
	priceList.append(soup.select('.totalPrice'))

for m in priceList:
	print '------'
	for n in m:
		print n.span.string