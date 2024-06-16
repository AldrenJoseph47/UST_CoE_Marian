import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["USTProject"]
mycol = mydb["Employees"]
myquery = { "Dept": "Marketing" }
newvalues = { "$set": { "Dept": "Testing" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
for x in mycol.find():
  print(x)