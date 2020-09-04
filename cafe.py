from flask import Flask,render_template,flash,redirect,url_for,session,logging,request,Response
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps


app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="mycafe"
app.config["MYSQL_CURSORCLASS"]="DictCursor" 
mysql = MySQL(app)

app.secret_key = "mycafe"
@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/about") 
def about():
    return render_template("about.html")


# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim soyisim",validators=[validators.length(min=4,max=25)])
    email = StringField("Email Adresi",validators=[validators.Email(message="Lütfen Geçerli bir mail adresi giriniz.")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin."),
        validators.EqualTo(fieldname="confirm",message = "Parolanız uyuşmuyor...")
    ])
    confirm = PasswordField("Parola Doğrulama")


# Login İşlemi
@app.route("/login",methods = ["GET","POST"])
def login():
    form = RegisterForm(request.form)
    if request.method == "POST":
        email = form.email.data
        password_entered = form.password.data
        
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM Customer WHERE CEmail = %s"
        result = cursor.execute(sorgu,(email,))
        if result > 0:
            data = cursor.fetchone()
            real_password = data["Password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla Giriş Yaptınız.","success")

                session["logged_in"] = True
                session["email"] = email
                return redirect(url_for("index"))
            else:
                flash("Parolanızı yanlış girdiniz.","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunamadı.","danger")
            return redirect(url_for("login"))

    return render_template("login.html",form=form)

# Kayıt Olma
@app.route("/register",methods=["GET","POST"])
def register ():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        sorgu = "INSERT INTO Customer(CustomerName,CEmail,Password) VALUES (%s,%s,%s)"
        sorgu1= "INSERT INTO orders(OrderID) SELECT CustomerID from customer Where CEmail=%s"
        cursor.execute(sorgu,(name,email,password))
        cursor.execute(sorgu1,(email,))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla Kayıt Olundu...","success")
        return redirect(url_for("login")) 
    else:
        return render_template("register.html",form=form)

# Logout İşlemi
@app.route("/logout")
def logout():
    session.clear()
    flash("Başarıyla Çıkış Yapıldı...","danger")
    return redirect(url_for("index"))



@app.route("/order")
def cart ():   
    cursor = mysql.connection.cursor()
    sorgu= "SELECT ProductID,ProductsName,UnitPrice FROM orderdetail WHERE Emails = %s"
    result=cursor.execute(sorgu,(session["email"],))

    if result > 0:
        meals = cursor.fetchall()
        return render_template("order.html",meals=meals)

    else:
        return render_template("order.html")

    return render_template("order.html")



@app.route("/menu",methods=["GET","POST"])
def menu ():
    if request.method == "POST":            
        cursor = mysql.connection.cursor()
        post_id = request.form['product']
        sorgu= "Select CustomerId From customer Where CEmail = %s"
        cursor.execute(sorgu,(session["email"],))
        customer_ID = cursor.fetchone()
        c1=customer_ID["CustomerId"]
        customer = "INSERT INTO orderdetail(Emails,orderdetail.OrderID,ProductID,ProductsName,UnitPrice) SELECT CEmail,orders.OrderID,ProductID,ProductName,ProductPrice FROM customer,orders,product WHERE Cemail=%s and orders.OrderID=%s and ProductID=%s"
        cursor.execute(customer,(session["email"],c1,post_id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("menu")) 
    else:
        return render_template("menu.html")



@app.route("/order",methods=["GET","POST"])
def delete():
    if request.method == "POST":    
        cursor = mysql.connection.cursor()
        post_id = request.form['deleteproduct']
        sorgu= "Select OrderdId From orderdetail Where ProductID = %s"
        cursor.execute(sorgu,(post_id,))
        food = cursor.fetchone()
        food1=food["OrderdId"]
        customer = "DELETE FROM orderdetail WHERE OrderdId=%s"
        cursor.execute(customer,(food1,))
        
        mysql.connection.commit()
        cursor.close()
        return cart()


    
        
if __name__ == "__main__":
    app.run(debug=True) 