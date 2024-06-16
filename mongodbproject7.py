import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["USTProject"]
mycol = db["employees"]
def calculate_salary(BP):
    HRA = 0.12 * BP
    GP = BP + HRA
    if GP < 2000:
        TAX = 0
    elif GP < 3000 and GP >2001:
        TAX = 0.02 * GP
    elif GP < 4000 and GP >3001:
        TAX = 0.03 * GP
    else:
        TAX = 0.05 * GP
    NP = GP - TAX
    return HRA, GP, TAX, NP
Empid = input("Enter Employee ID: ")
if mycol.find_one({"Empid": Empid}):
    print("Empid is already in use.")
else:
    BP = float(input("Enter Basic Pay: "))
    HRA, GP, TAX, NP = calculate_salary(BP)
    employee_data = {"Empid": Empid,"BP": BP,"HRA": HRA,"GP": GP,"TAX": TAX,"NP": NP}
    mycol.insert_one(employee_data)
    print("Employee data inserted successfully.")
    print("Empid:", Empid)
    print("Basic Pay:", BP)
    print("HRA:", HRA)
    print("GP:", GP)
    print("TAX:", TAX)
    print("NP:", NP)