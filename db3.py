import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe", cursorclass = pymysql.cursors.DictCursor)
try:
   with connection.cursor() as cursor:
    adding= "INSERT INTO Category(CategoryID,CategoryName) Values (0 , 'Çorbalar')" 
    adding1="INSERT INTO Category(CategoryID,CategoryName) Values (1 , 'Salatalar')"
    adding2= "INSERT INTO Category(CategoryID,CategoryName) Values(2, 'Makarnalar')"
    adding3= "INSERT INTO Category(CategoryID,CategoryName) Values(3, 'Pizzalar')"
    adding4= "INSERT INTO Category(CategoryID,CategoryName) Values(4, 'Et/Tavuk Yemekleri')"
    adding5= "INSERT INTO Category(CategoryID,CategoryName) Values(5, 'İçecekler')"
    adding6= "INSERT INTO Category(CategoryID,CategoryName) Values(6, 'Tatlılar')"

    cursor = connection.cursor()
    cursor.execute(adding)
    cursor.execute(adding1)
    cursor.execute(adding2)
    cursor.execute(adding3)
    cursor.execute(adding4)
    cursor.execute(adding5)
    cursor.execute(adding6)
    

    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")
