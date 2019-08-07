import pymongo

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

def GetCollectionName(version):
    db = client.Name
    collection = db.Name
    myQuery = {"Version":version}
    result = collection.find(myQuery,{"_id":0,"Version":0}) #,{"Name":1 ,"Version":0}
    for x in result:
        nameResult = x['Name']
    return nameResult


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
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is up " + str(diff / float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
            else:
                pro = back
                back = price[x]
                if pro >= back : ##降价
                    diff = pro - back
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is down " + str(diff / float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff/float(pro)>=0.3 :
                        print(i)
                        print("price is up "+str(diff/float(pro)))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
        pro = 0
        back = 0
        for z in range(0,len(number)):
            if z == 0:
                pro = number[z]
            elif x == 1:
                back = number[z]
                if pro >= back : ##减少库存
                    diff = pro - back
                    if diff > 20 :
                        print(i)
                        print("number is down "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
                else : #增加
                    diff = back - pro
                    if diff > 20 :
                        print(i)
                        print("number is up "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
            else:
                pro = back
                back = number[z]
                if pro >= back : ##降价
                    diff = pro - back
                    if diff > 20 :
                        print(i)
                        print("number is down "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
                else : #涨价
                    diff = back - pro
                    if diff >= 20 :
                        print(i)
                        print("number is up "+str(diff))
                        print("pro:"+str(pro)+"  back:"+str(back))
                    else:
                        print(i)
                        print("pro:"+str(pro)+"  back:"+str(back))
            #策略：数量波动超过50 / 价格波动超过40% 即可判断




