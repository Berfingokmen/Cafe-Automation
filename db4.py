import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe", cursorclass = pymysql.cursors.DictCursor)
try:
   with connection.cursor() as cursor:
    tableadding= "INSERT INTO Tables(TableID,TableName) Values (1 , 'Teras1')" 
    tableadding1="INSERT INTO Tables(TableID,TableName) Values (2 , 'Teras2')"

    tableadding2= "INSERT INTO Tables(TableID,TableName) Values (3 , 'Teras3')" 
    tableadding3="INSERT INTO Tables(TableID,TableName) Values (4 , 'Teras4')"
    tableadding4= "INSERT INTO Tables(TableID,TableName) Values (5 , 'Teras5')" 
    tableadding5="INSERT INTO Tables(TableID,TableName) Values (6, 'Bahçe1')"
    tableadding6= "INSERT INTO Tables(TableID,TableName) Values (7 , 'Bahçe2')" 
    tableadding7="INSERT INTO Tables(TableID,TableName) Values (8 , 'Bahçe3')"
    tableadding8= "INSERT INTO Tables(TableID,TableName) Values (9 , 'Bahçe4')" 
    tableadding9="INSERT INTO Tables(TableID,TableName) Values (10 , 'Bahçe5')"

    #Çorbalar
    productadding1="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (01,'Mercimek Çorbası',5 , 0)"
    productadding2="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (02,'Ezogelin Çorbası',5 , 0)"
    productadding3="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (03,'Yayla Çorbası',7 , 0)"
    productadding4="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (04,'Kremalı Mantar Çorbası',7 , 0)"
    #salatalar
    productadding5="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (11,'Sezar Salata',15 , 1)"
    productadding6="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (12,'Tavuklu Salata',18, 1)"
    productadding7="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (13,'Tonbalıklı Salata',18 , 1)"
    productadding8="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (14,'Izgara Biftekli Salata',25 , 1)"
    #makarnalar
    productadding9="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (21,'Pesto Soslu Tortelini',18 , 2)"
    productadding10="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (22,'Kremalı Mantarlı Makarna',18 , 2)"
    productadding11="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (23,'Köri Soslu Makarna',18 , 2)"
    productadding12="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (24,'Mac&Cheese',18, 2)"
    #pizzalar
    productadding13="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (31,'Vejeteryan Pizza',18 , 3)"
    productadding14="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (32,'Ton Balıklı Pizza',18 , 3)"
    productadding15="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (33,'Margarita',18 , 3)"
    productadding16="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (34,'Karışık Peynirli Pizza',18, 3)"
    #et/tavuk 
    productadding17="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (41,'Izgara Tavuk',22 , 4)"
    productadding18="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (42,'Kremalı Tavuk',25 , 4)"
    productadding19="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (43,'Tavuk Fajita',25 , 4)"
    productadding20="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (44,'Tavuk Şinitzel',25, 4)"
    productadding21="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (45,'Çökertme Kebabı',30 , 4)"
    productadding22="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (46,'Dana Antrikot',50 , 4)"
    productadding23="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (47,'Kaşarlı Köfte',30 , 4)"
    productadding24="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (48,'Et Sote',30, 4)"
    #içecekler
    productadding25="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (51,'Limonata',12 , 5)"
    productadding26="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (52,'Coca Cola',6 , 5)"
    productadding27="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (53,'Fanta',6 , 5)"
    productadding28="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (54,'Sprite',6, 5)"
    productadding29="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (55,'Ayran',6, 5)"
    productadding30="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (56,'Türk Kahvesi',8, 5)"
    productadding31="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (57,'Latte',12 , 5)"
    productadding32="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (58,'Milk Shake',12, 4)"
    #tatlılar
    productadding33="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (61,'Sufle',15 , 6)"
    productadding34="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (62,'Tiramisu',15 , 6)"
    productadding35="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (63,'San Sebastian ',18 , 6)"
    productadding36="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (64,'Karadutlu Orman Rüyası',18, 6)"
    productadding37="INSERT INTO Product(ProductID, ProductName , ProductPrice, CategoryId) Values (65,'Limonlu Cheesecake',18, 6)"


    cursor = connection.cursor()
    cursor.execute(tableadding)
    cursor.execute(tableadding1)
    cursor.execute(tableadding2)
    cursor.execute(tableadding3)
    cursor.execute(tableadding4)
    cursor.execute(tableadding5)
    cursor.execute(tableadding6)
    cursor.execute(tableadding7)
    cursor.execute(tableadding8)
    cursor.execute(tableadding9)
    cursor.execute(productadding1)
    cursor.execute(productadding2)
    cursor.execute(productadding3)
    cursor.execute(productadding4)
    cursor.execute(productadding5)
    cursor.execute(productadding6)
    cursor.execute(productadding7)
    cursor.execute(productadding8)
    cursor.execute(productadding9)
    cursor.execute(productadding10)
    cursor.execute(productadding11)
    cursor.execute(productadding12)
    cursor.execute(productadding13)
    cursor.execute(productadding14)
    cursor.execute(productadding15)
    cursor.execute(productadding16)
    cursor.execute(productadding17)
    cursor.execute(productadding18)
    cursor.execute(productadding19)
    cursor.execute(productadding20)
    cursor.execute(productadding21)
    cursor.execute(productadding22)
    cursor.execute(productadding23)
    cursor.execute(productadding24)
    cursor.execute(productadding25)
    cursor.execute(productadding26)
    cursor.execute(productadding27)
    cursor.execute(productadding28)
    cursor.execute(productadding29)
    cursor.execute(productadding30)
    cursor.execute(productadding31)
    cursor.execute(productadding32)
    cursor.execute(productadding33)
    cursor.execute(productadding34)
    cursor.execute(productadding35)
    cursor.execute(productadding36)
    cursor.execute(productadding37)
    
    
    

    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")
