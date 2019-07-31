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
