import pymongo
import math
client = pymongo.MongoClient(host="localhost",port=27017)

def insert(DBname,Name,Price,Number,Index):
    db = client[DBname]
    collection = db[Name]
    data = {
        "Price" : float(Price),
        "Number" : int(Number),
        "Index" : int(Index)
    }
    result = collection.insert(data)
    return result

def SaveName(Name):
    db = client.Name
    collection = db["Name"]
    data = {
        "Name" : Name
    }
    result = collection.insert(data)
    return result

'''
将网页中获取的存储在dbName(c5)db 中的collection名字读出作为一个索引
存入到Name db中
'''
def SaveCollectionName(dbName,version):
    db = client[dbName]
    collectionName = db.list_collection_names(session=None)
    dbS = client.Name
    collection = dbS.Name
    data = {
        "Name" : collectionName,
        "Version" : version
    }
    collection.insert(data)
    return collectionName


'''
存入collectionName
标注version
'''
def SetCollectionName(dbName,collectionName,version):
    db = client[dbName]
    collection = db.Name
    data = {
        "Name":collectionName,
        "Version":version
    }
    collection.insert(data)


'''
根据version来读取db-Name 中的collectionName
'''
def GetCollectionName(version):
    db = client.Name
    collection = db.Name
    myQuery = {"Version":version}
    result = collection.find(myQuery,{"_id":0,"Version":0}) #,{"Name":1 ,"Version":0}
    for x in result:
        nameResult = x['Name']
    return nameResult

'''
读取dbName中的数据根据MaxIndex来确定每个collection中document的数量
'''
def ReadData(dbName,MaxIndex):
    db = client[dbName]
    collectionName = db.list_collection_names(session=None)
    for i in collectionName:
        price = []
        number = []
        for index in range(1,MaxIndex+1):
            collection = db[i]
            query = {"Index":index}
            result = collection.find(query,{"_id":0,"Index":0})
            for x in result :
                price.append(x["Price"])
                number.append(x["Number"])
        pro = 0
        back = 0
        for x in range(0,len(price)):
            if x == 0:
                pro = price[x]
            elif x == 1:
                back = price[x]
                if pro >= back : ##降价
                    diff = pro - back
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is down " + str(diff / float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is up " + str(diff / float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
            else:
                pro = back
                back = price[x]
                if pro >= back : ##降价
                    diff = pro - back
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is down " + str(diff / float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is up "+str(diff/float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
        pro = 0
        back = 0
        for z in range(0,len(number)):
            if z == 0:
                pro = number[z]
            elif z == 1:
                back = number[z]
                if pro >= back : ##减少库存
                    diff = pro - back
                    if diff > 20 :
                        print(i)
                        print("number is down "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
                else : #增加
                    diff = back - pro
                    if diff > 20 :
                        print(i)
                        print("number is up "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
            else:
                pro = back
                back = number[z]
                if pro >= back : ##降价
                    diff = pro - back
                    if diff > 20 :
                        print(i)
                        print("number is down "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff >= 20 :
                        print(i)
                        print("number is up "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    # else:
                    #     print(i)
                    #     print("pro:"+str(pro)+"  back:"+str(back))
            #策略：数量波动超过50 / 价格波动超过40% 即可判断

'''
根据读取数据库中的数据 采取某一策略来更新需要监控的名称
返回一个list
'''
def GetNewCollectionName(dbName,MaxIndex):
    db = client[dbName]
    collectionName = db.list_collection_names(session=None)
    NewCollectionName = []
    for i in collectionName:
        flag = 0
        price = []
        number = []
        for index in range(1,MaxIndex+1):
            collection = db[i]
            query = {"Index":index}
            result = collection.find(query,{"_id":0,"Index":0})
            for x in result :
                price.append(x["Price"])
                number.append(x["Number"])
        ###取数量均值
        allNumber = 0
        for x in range(0,len(number)):
            allNumber = allNumber+number[x]
        avg = allNumber/len(number)
        if(avg < 20):
            continue

        proPrice = 0
        backPrice = 0
        proNumber = 0
        backNumber = 0
        avgPrice = 0
        avgNumber = 0
        for x in range(0,len(price)):
            if x == 0:
                proPrice = price[x]
                proNumber = number[x]
            elif x == 1:
                backPrice = price[x]
                backNumber = number[x]
                avgPrice =avgPrice + math.fabs(proPrice - backPrice)/float(proPrice)
                avgNumber = avgNumber + math.abs(proNumber - backNumber)

                # if proPrice >= backPrice : ##降价
                #     diffPrice = proPrice - backPrice
                #     avgPrice = avgPrice + diffPrice/float(proPrice)
                # else : #涨价
                #     diffPrice = backPrice - proPrice
                #     avgPrice = avgPrice + diffPrice/float(proPrice)
                # if proNumber >= backNumber:
                #     diffNumber = proNumber - backNumber
                #     avgNumber = avgNumber + diffNumber
                # else :
                #     diffNumber = backNumber - proNumber
                #     avgNumber =
            else:
                proPrice = backPrice
                backPrice = price[x]
                proNumber = backNumber
                backNumber = number[x]
                avgPrice =avgPrice + math.fabs(proPrice - backPrice)/float(proPrice)
                avgNumber = avgNumber + math.abs(proNumber - backNumber)

                # if proPrice >= backPrice : ##降价
                #     diffPrice = proPrice - backPrice
                #     avgPrice = avgPrice + diffPrice/float(proPrice)
                # else : #涨价
                #     diffPrice = backPrice - proPrice
                #     avgPrice = avgPrice + diffPrice/float(proPrice)
        avgNumber =avgNumber/float(len(number)-1)
        avgPrice = avgPrice/float(len(price)-1)
        if avgNumber >= 25 and avgPrice>=0.05 :
            flag = 1

        if flag == 1 :
            NewCollectionName.append(i)

    return NewCollectionName

'''
在更新了collectionName之后
将原来存储在c5中的数据进行删除，只保留新的collectionName中的数据
'''
def RenewDataDB(dbData,version):
    db = client[dbData]
    collectionAll = db.list_collection_names(session=None)
    collectionNew = GetCollectionName(version)
    for i in collectionAll:
        if i in collectionNew:
            print(i)
        else:
            mydb = client[dbData]
            mycol = mydb[i]
            mycol.drop()
