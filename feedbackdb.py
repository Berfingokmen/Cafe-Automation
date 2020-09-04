import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe", cursorclass = pymysql.cursors.DictCursor)
try:
   with connection.cursor() as cursor:
    sorgu = "CREATE TABLE IF NOT EXISTS Feedback(FID INT PRIMARY KEY, CID INT NOT NULL , rate INT NOT NULL, FBack TEXT NOT NULL  )"
   
    cursor = connection.cursor()
    cursor.execute(sorgu)
    connection.commit()

finally:
    connection.close()