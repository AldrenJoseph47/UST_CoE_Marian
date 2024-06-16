import pymongo
def connect_Python():
    global my_client
    global dblist
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist = my_client.list_database_names()
    print("THE LIST OF DATABASES")
    print(dblist)#prints the databases list

# function to print the first row in the MongoDB Database
def print_allRows():
    my_database=my_client["USTProject"]
    my_collection=my_database["Employees"]
    print("PRINT ALL THE ROW IN THE TABLE EMPLOYEES")
    for records in my_collection.find():
        #find() to have whole collection using for loop
        print(records)

def print_FirstRow():
    my_database=my_client["USTProject"]
    my_collection=my_database["Employees"]
    first_record =my_collection.find_one()
        #find_one() to fetch the first collection
    print("THE FIRST ROW OF THE TABLE USTProject")
    print(first_record)

def check_DatabaseExist():
    if "USTProject" in dblist:
        print("My Database Exist!!")

def print_specificColumns():
    my_database=my_client["USTProject"]

def print_rowsCriteria():
    my_database=my_client["USTProject"]
    my_collection=my_database["Employees"]
    my_query={"Dept":"Sales"}
    my_documents=my_collection.find(my_query)
    print("PRINTING A SPECIFIC ROW AS REQUIRED")
    for records in my_documents:
        print(records)

if __name__ == '__main__':
    connect_Python()
    check_DatabaseExist()
    print_allRows()
    print_FirstRow()
    print_rowsCriteria()
