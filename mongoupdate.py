import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["USTProject"]
mycol = mydb["Employees"]
myquery = { "Dept": "Training" }
newvalues = { "$set": { "Dept": "Canyon" } }
mycol.update_one(myquery, newvalues)
#print "Employees" after the update:
for x in mycol.find():
  print(x)
