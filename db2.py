import pymysql.cursors
import datetime

connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe", cursorclass = pymysql.cursors.DictCursor)

try: 
   with connection.cursor() as cursor:
    sqlQuery = "CREATE TABLE IF NOT EXISTS Category(CategoryId INT PRIMARY KEY, CategoryName TEXT NOT NULL )"
    sqlQuery5="CREATE TABLE IF NOT EXISTS Tables(TableID INT PRIMARY KEY, TableName TEXT NOT NULL)"
    sqlQuery2 ="CREATE TABLE IF NOT EXISTS Orders(OrderID INT PRIMARY KEY, OrderDate DATE NOT NULL, Orderstatus INT NOT NULL)"

    sqlQuery3 = "CREATE TABLE IF NOT EXISTS OrderDetail(OrderdId INT PRIMARY KEY, OrderID INT NOT NULL, ProductID INT NOT NULL, UnitPrice INT NOT NULL, Total INT NOT NULL )"
    sqlQuery4="CREATE TABLE IF NOT EXISTS Product(ProductID INT PRIMARY KEY, ProductName TEXT NOT NULL, ProductPrice double NOT NULL, CategoryId INT NOT NULL)"
    
    sqlQuery6="CREATE TABLE IF NOT EXISTS Employee(EmployeeID INT PRIMARY KEY, FName TEXT, LName TEXT, Salary double NOT NULL, PhoneNo INT NOT NULL)"
    sqlQuery7 = "CREATE TABLE IF NOT EXISTS Customer(CustomerId INT PRIMARY KEY, CustomerName TEXT NOT NULL, CEmail TEXT NOT NULL, Password TEXT NOT NULL,OrderId INT )"
    cursor.execute(sqlQuery)
    cursor.execute(sqlQuery5)
    cursor.execute(sqlQuery3)
    cursor.execute(sqlQuery4)
    cursor.execute(sqlQuery2)
    cursor.execute(sqlQuery6)
    cursor.execute(sqlQuery7)


         
finally:
    connection.close()
