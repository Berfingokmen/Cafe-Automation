import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe",port = 3306, cursorclass = pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:

        #sorgu1="ALTER TABLE Orders ADD COLUMN TableID INT"
        #sorgu = "ALTER TABLE Orders ADD FOREIGN KEY (TableID) REFERENCES Tables(TableID)"
        #sorgu2="ALTER TABLE OrderDetail ADD FOREIGN KEY(ProductID) REFERENCES Product(ProductID)"
        #sorgu3="ALTER TABLE OrderDetail ADD FOREIGN KEY(OrderID) REFERENCES Orders(OrderID)"
        #sorgu4="ALTER TABLE Product ADD FOREIGN KEY(CategoryId) REFERENCES Category(CategoryID) "
        #sorgu5="ALTER TABLE Customer ADD FOREIGN KEY(OrderId) REFERENCES Orders(OrderID)"
        #sorgu6="ALTER TABLE Orderdetail ADD FOREIGN KEY(OrderID) REFERENCES Customer(CustomerID)"
        sorgu7="ALTER TABLE Feedback ADD FOREIGN KEY(CID) REFERENCES Customer(CustomerID)"
      

        #cursor.execute(sorgu1)
        #cursor.execute(sorgu)
        #cursor.execute(sorgu2)
        #cursor.execute(sorgu3)
        #cursor.execute(sorgu4)
        #cursor.execute(sorgu5)
        #cursor.execute(sorgu6)
        cursor.execute(sorgu7)
       
        connection.commit()
finally:
     connection.close()