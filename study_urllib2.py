# -*- coding: utf-8 -*-
# @Author: oveleva
# @Date:   2020-03-22 13:38:50
# @Last Modified by:   lee
# @Last Modified time: 2020-03-22 14:39:55

import re
import urllib2
import cookielib
# import bs4
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

print '1'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '2'
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '3'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
html_doc = response3.read()
# print cj
# print html_doc

soup = BeautifulSoup(
                    html_doc,              # HTML文档字符串
                    'html.parser',         # HTML解析器
                    from_encoding = 'utf8' # HTML文档的编码
                    )

# find(name, attrs, string) find_all 查询所有
nodes = soup.find_all('a', href = re.compile(r'www'))

for link in nodes:
    # print link.name, link['href'], link.get_text()
    print link['href'], link.get_text()

