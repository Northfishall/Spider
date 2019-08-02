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
        for index in range(0,MaxIndex+1):
            collection = db[i]
            query = {"Index":index}
            


