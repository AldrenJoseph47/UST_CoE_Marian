import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["USTProject"]
mycol = mydb["customers"]
myquery = { "Email": "Alen.jerry@Gmail.com" }
mycol.delete_one(myquery)
