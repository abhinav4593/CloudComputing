from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2
from lxml import etree
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

BASE_URL = "http://www.cnet.com/products/microsoft-surface-pro-4/user-reviews/"
html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")
txt=str(soup)
prducttxt=soup.find("div",{"id":"modelInfo"})
prdct= prducttxt.prettify()
file = open("./htmlpretty.txt", "w")
file.write(prdct)
file.close()
pname=prducttxt.h3.string
pNumber=prducttxt.find("span" , "partNumber").string
productNumber= pNumber[13:]
print pname
print "--------"
print productNumber
print "--------"
#commentsbody=soup.find('div',{'id':'livefyreConversation'}).extract()
#commentslist=soup.findAll('article')
#commentsbody.find('div',{'class':'fyre fyre-reviews fyre-width-medium'})
#List = soup.find(class_="fyre fyre-reviews fyre-width-medium")
#t1=commentsbody.find("div",{'id':'livefyreConversation'})
#t2=commentsbody.find("div",{'class':'fyre-stream-content'})
#print commentslist[0]
#t2=soup.find("div",{"id":"livefyreContainer"})
#t3=t2.find("class",'fyre-stream-content')
#print t3
#for div in soup.findAll('div', attrs={'class':'fyre-stream-content'}):
txt=soup.find('div',{'id':'livefyreConversation'}).div
print txt


