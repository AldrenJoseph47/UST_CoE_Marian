import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb =  myclient["USTProject"]
mycol = mydb["Employees"]
mydoc =mycol.find().sort("EmpName")
for x in mydoc:
    print(x)



#x = mycol.insert_one(mydoc)
#= {"EmpID": "19015","EmpName": "Alen jerry","Dept": "testing","Email": "Alen.jerry@Gmail.com"}