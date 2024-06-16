import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["USTProject"]
mycol = mydb["Employees"]
myquery = { "Email": {"$regex": "^G"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")