# -*- coding: utf-8 -*-
import re
import MongoDB

#Testfile = open("d://c5Data1.txt","r",encoding="UTF-8").read()
Testfile = open("d://Nice.txt","r",encoding="UTF-8").read()

#req  =  r'title="(.+?)"'
'''
req = r'<li class="selling">([\n.]+?)</li>'

reqT = re.compile(req)
matchlist = re.findall(reqT,Testfile)

print(matchlist)
'''

# req = r'<li class="selling">(.+?)</li>'
# nameR = r'<span class=" .+? ">(.+?)</span>'
# priceR = r'<span class="price">￥ (.+?)</span>'
# numberR = r'<span class="num">(.+?)</span>'
# soleR = r'^([0-9]+?)[^0-9]+'
# soleRC = re.compile(soleR)
# reqT = re.compile(req)
# matchlist = re.findall(req,Testfile,re.S)
#
# for i in matchlist:
#     name = re.findall(nameR,i,re.S)
#     price = re.findall(priceR,i,re.S)
#     numberO = re.findall(numberR,i,re.S)
#     number = re.findall(soleRC, numberO[0])[0]
#     MongoDB.insert("c5",name[0],price[0],number,1)
#
#     print(name[0])
#     print(price[0])
#     print(number)
#     print(re.findall(soleRC, numberO[0])[0])



req = r'<div class="sneakerItem"(.+?)</div></div></div>'
name = r'<div class="bottom">(.+?)$'
number = r'<div class="count">(.+?)[^0-9]+</div></div>'
price = r'<div class="num">(.+?)</div></div>'
id = r'gid="(.+?)"'

matchlist = re.findall(req,Testfile, re.S)
index = 0
for i in matchlist:
    print (i)
    if index == 1:
        index = index +1
        continue
    print(re.findall(id,i,re.S))
    id = re.findall(id, i, re.S)[0]
    price = re.findall(price, i, re.S)[0]
    name = re.findall(name, i, re.S)[0]
    number = re.findall(number, i, re.S)[0]
    print("Name:"+name)
    print("Price:"+price)
    print("Number:"+number)
    print("ID:"+id)
    index = index +1