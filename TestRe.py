# -*- coding: utf-8 -*-
import re
import MongoDB

Testfile = open("d://c5Data1.txt","r",encoding="UTF-8").read()


#req  =  r'title="(.+?)"'
'''
req = r'<li class="selling">([\n.]+?)</li>'

reqT = re.compile(req)
matchlist = re.findall(reqT,Testfile)

print(matchlist)
'''

req = r'<li class="selling">(.+?)</li>'
nameR = r'<span class=" .+? ">(.+?)</span>'
priceR = r'<span class="price">￥ (.+?)</span>'
numberR = r'<span class="num">(.+?)</span>'
soleR = r'^([0-9]+?)[^0-9]+'
soleRC = re.compile(soleR)
reqT = re.compile(req)
matchlist = re.findall(req,Testfile,re.S)

for i in matchlist:
    name = re.findall(nameR,i,re.S)
    price = re.findall(priceR,i,re.S)
    numberO = re.findall(numberR,i,re.S)
    number = re.findall(soleRC, numberO[0])[0]
    MongoDB.insert("c5",name[0],price[0],number,1)

    print(name[0])
    print(price[0])
    print(number)
    print(re.findall(soleRC, numberO[0])[0])