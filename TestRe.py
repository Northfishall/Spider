# -*- coding: utf-8 -*-
import re
import nice
import MongoDB

#Testfile = open("d://c5Data1.txt","r",encoding="UTF-8").read()
#Testfile = open("d://Nice.txt","r",encoding="UTF-8").read()

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

data = '''<div class="basic-info cmn-clearfix">
<dl class="basicInfo-block basicInfo-left">
<dt class="basicInfo-item name">中文名</dt>
<dd class="basicInfo-item value">
钱学森
</dd>
<dt class="basicInfo-item name">外文名</dt>
<dd class="basicInfo-item value">
Tsien Hsue-shen(<a target="_blank" href="/item/%E9%9F%A6%E6%B0%8F%E6%8B%BC%E9%9F%B3">韦氏拼音</a>）,Qian Xuesen（<a target="_blank" href="/item/%E6%B1%89%E8%AF%AD%E6%8B%BC%E9%9F%B3">汉语拼音</a>）
</dd>
<dt class="basicInfo-item name">国&nbsp;&nbsp;&nbsp;&nbsp;籍</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD">中国</a>
</dd>
<dt class="basicInfo-item name">民&nbsp;&nbsp;&nbsp;&nbsp;族</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E6%B1%89%E6%97%8F">汉族</a>
</dd>
<dt class="basicInfo-item name">出生地</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E4%B8%8A%E6%B5%B7">上海</a>
</dd>
<dt class="basicInfo-item name">出生日期</dt>
<dd class="basicInfo-item value">
1911年（<a target="_blank" href="/item/%E8%BE%9B%E4%BA%A5/26230" data-lemmaid="26230">辛亥</a>年）12月11日
</dd>
<dt class="basicInfo-item name">逝世日期</dt>
<dd class="basicInfo-item value">
2009年（<a target="_blank" href="/item/%E5%B7%B1%E4%B8%91">己丑</a>年）10月31日
</dd>
<dt class="basicInfo-item name">毕业院校</dt>
<dd class="basicInfo-item value">
国立交通大学、<a target="_blank" href="/item/%E5%8A%A0%E5%B7%9E%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2">加州理工学院</a>
</dd>
<dt class="basicInfo-item name">信&nbsp;&nbsp;&nbsp;&nbsp;仰</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E5%85%B1%E4%BA%A7%E4%B8%BB%E4%B9%89">共产主义</a>
</dd>
</dl><dl class="basicInfo-block basicInfo-right">
<dt class="basicInfo-item name">主要成就</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E8%88%AA%E5%A4%A9%E4%B9%8B%E7%88%B6">中国航天之父</a>
<br><a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E5%AF%BC%E5%BC%B9%E4%B9%8B%E7%88%B6">中国导弹之父</a>
<br><a target="_blank" href="/item/%E7%81%AB%E7%AE%AD%E4%B9%8B%E7%8E%8B">火箭之王</a>
<br>中国自动化控制之父
<br>“<a target="_blank" href="/item/%E4%B8%A4%E5%BC%B9%E4%B8%80%E6%98%9F%E5%8A%9F%E5%8B%8B%E5%A5%96%E7%AB%A0">两弹一星功勋奖章</a>”
<a class="toggle toExpand"><em class="arrow arrow-border"></em><em class="arrow arrow-bg"></em>展开</a>
<div class="basicInfo-overlap">
<dl class="basicInfo-block overlap">
<dt class="basicInfo-item name">主要成就</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E8%88%AA%E5%A4%A9%E4%B9%8B%E7%88%B6">中国航天之父</a>
<br><a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E5%AF%BC%E5%BC%B9%E4%B9%8B%E7%88%B6">中国导弹之父</a>
<br><a target="_blank" href="/item/%E7%81%AB%E7%AE%AD%E4%B9%8B%E7%8E%8B">火箭之王</a>
<br>中国自动化控制之父
<br>“<a target="_blank" href="/item/%E4%B8%A4%E5%BC%B9%E4%B8%80%E6%98%9F%E5%8A%9F%E5%8B%8B%E5%A5%96%E7%AB%A0">两弹一星功勋奖章</a>”
<br>
<a target="_blank" href="/item/%E5%9B%BD%E5%AE%B6%E6%9D%B0%E5%87%BA%E8%B4%A1%E7%8C%AE%E7%A7%91%E5%AD%A6%E5%AE%B6">国家杰出贡献科学家</a>
<br>中国绿色贡献终身成就奖
<br>中国科学院自然科学奖一等奖
<br>“中国科学院<a target="_blank" href="/item/%E8%B5%84%E6%B7%B1%E9%99%A2%E5%A3%AB">资深院士</a>”
<br>“中国工程院资深院士”
<a class="toggle toCollapse"><em class="arrow arrow-border"></em><em class="arrow arrow-bg"></em>收起</a>
</dd>
</dl>
</div>
</dd>
<dt class="basicInfo-item name">代表作品</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E5%B7%A5%E7%A8%8B%E6%8E%A7%E5%88%B6%E8%AE%BA">工程控制论</a>、<a target="_blank" href="/item/%E7%89%A9%E7%90%86%E5%8A%9B%E5%AD%A6%E8%AE%B2%E4%B9%89">物理力学讲义</a>、<a target="_blank" href="/item/%E6%98%9F%E9%99%85%E8%88%AA%E8%A1%8C%E6%A6%82%E8%AE%BA">星际航行概论</a>、<a target="_blank" href="/item/%E8%AE%BA%E7%B3%BB%E7%BB%9F%E5%B7%A5%E7%A8%8B">论系统工程</a>
</dd>
<dt class="basicInfo-item name">夫&nbsp;&nbsp;&nbsp;&nbsp;人</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E8%92%8B%E8%8B%B1">蒋英</a>
</dd>
<dt class="basicInfo-item name">祖&nbsp;&nbsp;&nbsp;&nbsp;籍</dt>
<dd class="basicInfo-item value">
浙江省杭州市<a target="_blank" href="/item/%E4%B8%B4%E5%AE%89%E5%B8%82">临安市</a>
</dd>
<dt class="basicInfo-item name">儿&nbsp;&nbsp;&nbsp;&nbsp;子</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E9%92%B1%E6%B0%B8%E5%88%9A">钱永刚</a>
</dd>
<dt class="basicInfo-item name">父&nbsp;&nbsp;&nbsp;&nbsp;亲</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E9%92%B1%E5%9D%87%E5%A4%AB">钱均夫</a>
</dd>
</dl></div>'''

'''
range 边界变化test
###########结论############
range中的边界 只以第一次的输入为准 之后变动不会改变range中的数据
test = 10
for i in range(0,test):
    test = test - 1
    print(i)
print(test)
'''
reqName = r'<dt class="basicInfo-item name">(.+?)</dt>'
reqValue = r'<dd class="basicInfo-item value">(.+?)</dd>'
# 带链接关键词的获取
reqBluePart = r'<a target="_blank" href="/item/.+?">(.+?)</a>'

resultDiction = {'key':'value'}

matchlistKey = re.findall(reqName, data, re.S)
matchlistValue = re.findall(reqValue, data, re.S)
if len(matchlistKey)>len(matchlistValue):
    length = len(matchlistKey)
    for index in range(0,length):
        print(length)
        print(index)
        if index!=length-1:
            if matchlistKey[index]==matchlistKey[index+1]:
                del matchlistKey[index]
                length = length - 1
            continue
        break

rer = r'<a target="_blank" href="/item/.+?">'
reexp = r'dd class="basicInfo-item value">(.+?)<a class="toggle toCollapse">'
for i , j in zip(matchlistKey,matchlistValue):
    print(i)
    print(j)
    rekey = r'&nbsp;'
    key = re.sub(rekey," ",i)
    valueExp = re.findall(reexp,j,re.S)
    if len(valueExp)!=0:
        for valueExp in valueExp:
            datalist = valueExp.split('<br>')
            valuelist=[]
            for value in datalist:
                result = re.sub(rer, "", value)
                result = re.sub(r'<a.+?</a>', "", result)
                result = re.sub(r'<.+?>', "", result)
                result = re.sub(r'\n', "", result)
                valuelist.append(result)
    else:
        datalist = j.split('<br>')
        valuelist = []
        for value in datalist:
            result = re.sub(rer, "", value)
            result = re.sub(r'<a.+?</a>', "", result)
            result = re.sub(r'<.+?>',"",result)
            result = re.sub(r'\n',"",result)
            valuelist.append(result)
    resultDiction[key]=valuelist

print(resultDiction)
'''
rer = r'<a target="_blank" href="/item/.+?">'
test = re.findall(rer,data,re.S)
print(test)
for i in value:
    #print(str(index)+":"+i)
    datalist = data.split('<br>')
    for j in datalist:
        print(index)
        index = index + 1
        result = re.sub(rer, "", j)
        result = re.sub(r'<a.+?</a>', "", j)
        result = re.sub(r'<.+?>',"",j)
        print(result)
'''
#data = re.sub(rer,"",data)
#data = re.sub(r'<a.+?</a>',"",data)
#data = re.sub(r'</a>',"",data)
#data1 = data.replace(/<a target="_blank" href="/item/.+?"/g,"")
#print(data)
''''
matchlist = re.findall(req,Testfile, re.S)
for i in matchlist:
    print(i)
for i in matchlist:
    idR = re.findall(id, i, re.S)[0]
    priceR = re.findall(price, i, re.S)[0]
    nameR = re.findall(name, i, re.S)[0]
    numberR = re.findall(number, i, re.S)[0]
    print("Name:"+nameR)
    print("Price:"+priceR)
    print("Number:"+numberR)
    print("ID:"+idR)
    MongoDB.insert("nice", nameR, priceR, numberR, 1)
'''