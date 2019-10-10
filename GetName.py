# -*- coding: UTF-8 –*-
import SpiderLib
import time
import re
import MongoDB
import time
import random
from urllib.parse import quote
#{'rsv_re_ename':'蒋英','rsv_re_uri':'7166223'}
#https://www.google.com/search?sxsrf=ACYBGNSjEVQS_O1HOnAVzwVnKBUUyojClA%3A1569981999765&ei=LwaUXc6mLvHUmAWilJb4Bw&q=howt&oq=howt&gs_l=psy-ab.3..35i362i39l10.12607.14238..14462...3.0..1.348.1389.0j3j2j1......0....1..gws-wiz.....10..35i39j0j0i12j0i203j0i10.yVHFJHa67Y8&ved=0ahUKEwiO-pjbvvzkAhVxKqYKHSKKBX8Q4dUDCAo&uact=5
#req = r'<div class="fl ellip oBrLN" data-original-name="(.+?)">'
#<a target="_blank" title="蒋英" href="/s?rsv_idx=1&amp;wd=%E8%92%8B%E8%8B%B1&amp;usm=5&amp;ie=utf-8&amp;rsv_cq=%E9%92%B1%E5%AD%A6%E6%A3%AE&amp;rsv_dl=0_right_recommends_merge_28335&amp;euri=7166223"
reqName = r"{'rsv_re_ename':'(.+?)','rsv_re_uri'"
reqUrl = r'<a target="_blank" title=".+?" href="(.+?)"'
#url = "https://www.google.com.hk/search?safe=strict&source=hp&ei=NQWSXbb_LbyWr7wPsKSksAY&q=钱学森&oq=钱学森&gs_l=mobile-gws-wiz-hp.3..0l8.507.7084..7461...7.0..10.944.12501.2-4j11j9j5j1......0....1.......0..30i10j0i10j0i12.3SMtvTFybBY"
#url = "https://www.google.com/search?q=钱学森&oq=钱学森&aqs=chrome..69i57j0l5.1575j0j8&sourceid=chrome&ie=UTF-8"
#url = 'https://www.google.com/search?q=钱学森&oq=钱学森&aqs=chrome..69i57j69i60.4386j0j7&sourceid=chrome&ie=UTF-8'
#url = "https://www.google.com.hk/"
#url = "https://www.baidu.com/"
#web = SpiderLib.visitByProxyRef(url,url)
#print(web.data)
# web = SpiderLib.visitByLocalNet(url)
#web = SpiderLib.visitByLocalNet(url)
# print(web)
# matchlistName = re.findall(reqName,web.data.decode("UTF-8"), re.S)
# matchlistUrl = re.findall(reqUrl,web.data.decode("UTF-8"),re.S)
# for i ,j in zip(matchlistName,matchlistUrl):
#     print(i)
#     print(j)

'''
总体思路
从某个人名开始 获取与他相关的人的名称以及链接
1 人名进行映射
2 存储这些关系
3 搜索相关的名称重复步骤

在进行重复步骤的时候：
1 查看是否已经在表中并且已经搜索 如果已经在表中则直接跳过
'''

def Begin(url):
    mapIndex = 2
    NameList = ["钱学森"]
    mapName = {"钱学森":"1"}
    ConnectionRelationship = []
    NameQueue = []
    UrlQueue = []
    ConnectLength = []
    CurrentName = []
    CurrentName.append("钱学森")
    reqName = r"{'rsv_re_ename':'(.+?)','rsv_re_uri'"
    reqUrl = r'<a target="_blank" title=".+?" href="(.+?)"'
    reqBaike = r'mu="https://baike.baidu.com(.+?)"'
    ###########先将第一个节点的数据读取写入数据库
    web = SpiderLib.visitByLocalNet(url)
    matchlistbaike = re.findall(reqBaike, web.data.decode("UTF-8"), re.S)
    urlbaike = "https://baike.baidu.com" + matchlistbaike[0]
    print(urlbaike)
    urlbaike = quote(urlbaike,safe='/:?=&$@+,;%')
    info = GetBaikeData(urlbaike, 1)
    MongoDB.insertDictionary("Network", "Information", info)
    ### 写入数据库
    ####获取相关节点
    matchlistName = re.findall(reqName, web.data.decode("UTF-8"), re.S)
    matchlistUrl = re.findall(reqUrl, web.data.decode("UTF-8"), re.S)
    #由于url的格式相同 会获取下方热搜的url 导致混淆 er
    for i in range(len(matchlistName),len(matchlistUrl)):
        del matchlistUrl[len(matchlistName)]
    ConnectLength.append(len(matchlistName))
    NameQueue = NameQueue + matchlistName
    UrlQueue = UrlQueue + matchlistUrl
    while 1==1:
        if len(NameQueue)==0 :
            break
        time.sleep(random.randint(2,10))
        currentNode = CurrentName[0]
        currentIndex = mapName[currentNode]
        currentLength = ConnectLength[0]
        del CurrentName[0]
        del ConnectLength[0]
        for i in range(0,currentLength):
            print(mapName)
            print(ConnectionRelationship)
            if NameQueue[0] in NameList:
                ###之前已经获取过数据所以直接添加边即可
                indexB = mapName[NameQueue[0]]
                ConnectionRelationship.append([currentIndex,indexB])
            elif mapIndex>50:
                time.sleep(random.randint(10, 60))
                url = "https://www.baidu.com" + UrlQueue[0]
                print(NameQueue[0])
                print(UrlQueue[0])
                url = quote(url, safe='/:?=&$@+,;%')
                web = SpiderLib.visitByLocalNet(url)
                # 查询百度百科数据然后进行存储
                matchlistbaike = re.findall(reqBaike, web.data.decode("UTF-8"), re.S)
                if len(matchlistbaike)==0:
                    #没有对应的百度百科词条
                    info = {"id":mapIndex}
                    MongoDB.insertDictionary("Network","Information",info)
                else:
                    urlbaike = "https://baike.baidu.com" + matchlistbaike[0]
                    urlbaike = quote(urlbaike,safe='/:?=&$@+,;%')
                    info = GetBaikeData(urlbaike, mapIndex)
                    MongoDB.insertDictionary("Network", "Information", info)
                    #添加边
                ConnectionRelationship.append([currentIndex,str(mapIndex)])
                mapName[NameQueue[0]] = str(mapIndex)
                NameList.append(NameQueue[0])
                mapIndex = mapIndex+1
            else:
                time.sleep(random.randint(10, 60))
                print(NameQueue[0])
                print(UrlQueue[0])
                url = "https://www.baidu.com"+UrlQueue[0]
                url = quote(url, safe='/:?=&$@+,;%')
                web = SpiderLib.visitByLocalNet(url)
                # 查询百度百科数据然后进行存储
                matchlistbaike = re.findall(reqBaike, web.data.decode("UTF-8"), re.S)
                if len(matchlistbaike)==0:
                    #没有对应的百度百科词条
                    info = {"id":mapIndex}
                    MongoDB.insertDictionary("Network","Information",info)
                else:
                    urlbaike = "https://baike.baidu.com" + matchlistbaike[0]
                    urlbaike = quote(urlbaike,safe='/:?=&$@+,;%')
                    info = GetBaikeData(urlbaike, mapIndex)
                    MongoDB.insertDictionary("Network", "Information", info)
                #添加id以及边
                ConnectionRelationship.append([currentIndex,str(mapIndex)])
                mapName[NameQueue[0]] = str(mapIndex)
                NameList.append(NameQueue[0])
                mapIndex = mapIndex+1
                #添加该人物的相关人物 4个list
                matchlistName = re.findall(reqName, web.data.decode("UTF-8"), re.S)
                matchlistUrl = re.findall(reqUrl, web.data.decode("UTF-8"), re.S)
                # 由于url的格式相同 会获取下方热搜的url 导致混淆 er
                for i in range(len(matchlistName), len(matchlistUrl)):
                    del matchlistUrl[len(matchlistName)]
                if len(matchlistName)==0:
                    print("no relationNode")
                else:
                    ConnectLength.append(len(matchlistName))
                    CurrentName.append(NameQueue[0])
                    NameQueue = NameQueue + matchlistName
                    UrlQueue = UrlQueue + matchlistUrl
            del NameQueue[0]
            del UrlQueue[0]
    MongoDB.insertDictionary("Network","Map",mapName)
    MongoDB.insertlist("Network","Relation",ConnectionRelationship)


'''
<dd id="open-tag-item">
<span class="taglist">
文学家
</span>
，<span class="taglist">
人物
</span>
</dd>
'''
def GetBaikeData(url,id):
    print(url)
    web = SpiderLib.visitByLocalNet(url)
    reqBasicInfo = r'<div class="basic-info cmn-clearfix">(.+?)</div>'
    reqTag = r'<span class="taglist">\n(.+?)\n</span>'
    resultDiction = {'id': str(id)}
    matchlistTag = re.findall(reqTag,web.data.decode("UTF-8"),re.S)
    print(matchlistTag)
    if len(matchlistTag)==0:
        resultDiction['tag']=['Null']
    else:
        Tags = []
        for i in matchlistTag:
            reT = r'<a target="_blank" href=.+?">(.+?)</a>'
            tags = re.findall(reT,i,re.S)
            if len(tags)!=0:
                Tags.append(tags[0])
            else:
                Tags.append(i)
        resultDiction['tag']=Tags
    matchlistBasicInfo = re.findall(reqBasicInfo,web.data.decode("UTF-8"),re.S)
    if len(matchlistBasicInfo)==0:
        return resultDiction
    for data in matchlistBasicInfo:
        reqName = r'<dt class="basicInfo-item name">(.+?)</dt>'
        reqValue = r'<dd class="basicInfo-item value">(.+?)</dd>'
        # 带链接关键词的获取
        matchlistKey = re.findall(reqName,data,re.S)
        matchlistValue = re.findall(reqValue,data,re.S)
        if len(matchlistKey) > len(matchlistValue):
            length = len(matchlistKey)
            for index in range(0, length):
                print(length)
                print(index)
                if index != length - 1:
                    if matchlistKey[index] == matchlistKey[index + 1]:
                        del matchlistKey[index]
                        length = length - 1
                        if index == length - 1:
                            break
                    continue
                break
        rer = r'<a target="_blank" href="/item/.+?">'
        reexp = r'dd class="basicInfo-item value">(.+?)<a class="toggle toCollapse">'
        for i, j in zip(matchlistKey, matchlistValue):
            print(i)
            print(j)
            rekey = r'&nbsp;'
            key = re.sub(rekey, " ", i)
            valueExp = re.findall(reexp, j, re.S)
            if len(valueExp) != 0:
                for valueExp in valueExp:
                    datalist = valueExp.split('<br>')
                    valuelist = []
                    for value in datalist:
                        result = re.sub(rer, "", value)
                        result = re.sub(r'<.+?>', "", result)
                        result = re.sub(r'\n', "", result)
                        valuelist.append(result)
            else:
                datalist = j.split('<br>')
                valuelist = []
                for value in datalist:
                    result = re.sub(rer, "", value)
                    result = re.sub(r'<.+?>', "", result)
                    result = re.sub(r'\n', "", result)
                    valuelist.append(result)
            resultDiction[key] = valuelist
    return resultDiction
        #
        # Info = {'Key':'Value'}
        # for j ,k in zip(matchlistKey,matchlistValue):
        #     print(j)
        #     print(k)
        #     NameData = k.split('<br>')
        #     if NameData.len()==1:
        #         NameData = NameData[0].spile('、')
        #     #根据不同结构进行分割
        #     #if NameData.len()==1:
        #     #if

url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%92%B1%E5%AD%A6%E6%A3%AE&rsv_pq=b22f118500012251&rsv_t=c937i5VpLUOK0iEPgcKs34JamaZ%2Fn481E%2BCTb6TFBhQ%2F%2Ftuah5%2BuCFpQL6E&rqlang=cn&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=9&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&prefixsug=qianxues&rsp=0&inputT=3070&rsv_sug4=6298'

Begin(url)