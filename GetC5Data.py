# -*- coding: utf-8 -*-
import SpiderLib
import MongoDB

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
'''


def GetByPage():
    for i in range (1,10):
        url = "https://www.c5game.com/dota.html?rarity=immortal&page="+str(i)
        web = SpiderLib.visitByLocalNet(url)
        f = open('d://c5Data'+str(i)+'.txt', 'wb')
        f.write(web.data)
        SpiderLib.getC5TextData(web,1)

def GetByName(Name):
    url = "https://www.c5game.com/dota.html?min=&max=&k="+Name+"&rarity=&quality=unique&hero=&tag=&sort=&page=1"
    web = SpiderLib.visitByLocalNet(url)
    f = open('d://Search'+Name+'.txt', 'wb')
    f.write(web.data)
    SpiderLib.getC5TextData(web, 1)




#GetByPage()

GetByName("轮盘吉兆")