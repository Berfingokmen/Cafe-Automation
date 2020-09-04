import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "mycafe", cursorclass = pymysql.cursors.DictCursor)
try:
   with connection.cursor() as cursor:
    f1= "INSERT INTO feedback(FID,rate,Fback) Values (1,5 , 'Yemekleriniz harikaydı!')" 
    f2= "INSERT INTO feedback(FID,rate,Fback) Values (2,4 , 'Servisi çok beğendik')"
    f3= "INSERT INTO feedback(FID,rate,Fback) Values (3,1 , 'Yemekler geç geldi!!')" 
    

    cursor = connection.cursor()
    cursor.execute(f1)
    cursor.execute(f2)
    cursor.execute(f3)


    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")
