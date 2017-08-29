#!/usr/bin/python
#  -*- coding: UTF-8 -*-

import re

# 在其实位置匹配
print (re.match('www', 'www.qq.com').span())
# 不在其实位置匹配
print (re.match('com', ''))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"