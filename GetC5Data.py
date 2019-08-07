# -*- coding: utf-8 -*-
import sys
sys.path.append(".")
import SpiderLib
import MongoDB
import time
import random
import os
from urllib.parse import quote
import string

'''
BUFF data Type
<a href="/market/goods?goods_id=7903&amp;from=market#tab=selling" title="铭刻 噬魔之王">
<strong class="f_Strong">￥137</strong>

<a href="/market/goods?goods_id=4694&amp;from=market#tab=selling" title="铭刻 刑受神杖">
<strong class="f_Strong">￥5<small>.15</small></strong>

'''

#url = "https://buff.163.com/market/?game=dota2"
'''
url = "https://www.c5game.com/dota.html?rarity=immortal&page=2"
web = SpiderLib.visitByLocalNetRef(url,url)
SpiderLib.getBuffTextData(web)



f = open('d://C5PageImm2.txt', 'wb')
f.write(web.data)

'''


'''
https://www.c5game.com/dota/553443669-S.html 
https://www.c5game.com/dota/20300-S.html
https://www.c5game.com/dota/553443940-S.html

https://www.c5game.com/dota/553443749-S.html

https://www.c5game.com/dota.html?min=&max=&k=名称&rarity=&quality=unique&hero=&tag=&sort=&page=1

https://www.c5game.com/dota.html?rarity=immortal&page=1&quality=unique

https://www.c5game.com/dota.html?quality=unique&hero=&type=&exterior=&rarity=immortal&page=1
'''


def GetByPage():
    for i in range (1,20):
        #url = "https://www.c5game.com/dota.html?rarity=immortal&page="+str(i)
        url = "https://www.c5game.com/dota.html?quality=unique&hero=&type=&exterior=&rarity=immortal&page="+str(i)
        web = SpiderLib.visitByLocalNet(url)
        f = open('d://c5Data'+str(i)+'.txt', 'wb')
        f.write(web.data)
        SpiderLib.getC5TextData(web,1)
        time.sleep(random.randint(5,8))

def GetByName(Name,Index):
    url = "https://www.c5game.com/dota.html?min=&max=&k="+Name+"&rarity=&quality=unique&hero=&tag=&sort=&page=1"
    url = quote(url, safe=string.printable)
    print(url)
    web = SpiderLib.visitByLocalNet(url)
    if(web == "error"):
        print("exit")
        os._exit(0)
    else:
        f = open('d://Search'+Name+'.txt', 'wb')
        f.write(web.data)
        SpiderLib.getC5TextData(web,Index)
##根据Name数据库中的列表进行搜索
def SearchByList(version,Index):
    CollectionName = MongoDB.GetCollectionName(version)
    print(CollectionName)
    for i in CollectionName:
        GetByName(i,Index)
        time.sleep(random.randint(4,10))


SearchByList(1,3)
#MongoDB.ReadData("c5",2)


#CollectionName = MongoDB.SaveCollectionName("c5",1)
#print(CollectionName)

#GetByPage()

#GetByName("轮盘吉兆",-1)