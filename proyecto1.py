import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
name = "Nicolas Barbato"
app.secret_key = "brewing_clave"

def get_db_conection():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

posts = []

@app.route('/')
def home():
    conn, cursor = get_db_conection()
    cursor.execute("SELECT * FROM posts")
    post = cursor.fetchall()
    return render_template("home.html", posts=post)



@app.route("/sobre_nosotros")
def sobre_nosotros():
    return render_template("sobre_nosotros.html")  

@app.route("/login", methods=["GET", "POST"])
def login():
     if request.method == "GET":
        return render_template("login.html")
     elif request.method == "POST":
         username = request.form["username"]
         password = request.form["password"]
         conn,cursor = get_db_conection()
         cursor.execute("SELECT * FROM users WHERE users.username == ?", (username,))
         user_exist = cursor.fetchone()
         conn.close()
         if user_exist and user_exist[2] == password :
             session["username"] = username
             return render_template("perfil.html")
         else:
             return render_template("login.html", error = "Usuario o contraseña incorrectos")
         
         

@app.route("/perfil")
def perfil():
    username = session.get("username")
    if not username:
        return render_template("login.html", error = "Debe iniciar sesion para ver este perfil")
    return render_template("perfil.html", username=username)

@app.route("/logout")
def logout():
    username = session.get("username")
    if not username:
        return render_template("login.html", error = "Debe iniciar sesion")
    session.pop("username", None)
    return redirect("/")
    

@app.route("/create_post", methods=["GET","POST"])
def create_post():
        if request.method == "GET":
            username = session.get("username")
            if not username:
                return render_template("login.html", error = "Debe iniciar sesion para crear un nuevo post")
            return render_template("create_post.html")
        elif request.method == "POST":
            username = session.get("username")
            if not username:
                return render_template("login.html", error = "Debe iniciar sesion para crear un nuevo post")
            autor = username
            titulo = request.form["titulo"]
            posteo = request.form["posteo"]
            if autor and titulo and posteo:
                    conn, cursor = get_db_conection()
                    cursor.execute("INSERT INTO posts (autor, titulo, posteo) VALUES (?,?,?)", (autor, titulo, posteo))
                    conn.commit()
                    conn.close()
            return redirect('/')
            


@app.route("/post", methods=["GET", "POST"])
def post():
    return render_template("post.html")

@app.route("/post/<id>")
def busqueda(id):
    conn, cursor = get_db_conection()
    cursor.execute("SELECT * FROM posts WHERE posts.id == ?", id)
    post = cursor.fetchone()
    return render_template("post.html", post=post)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not password or not username:
            return render_template("register.html", error="USERNAME y PASSWORD son obligatorios")
        
        conn, cursor = get_db_conection()
        cursor.execute("SELECT * FROM users WHERE users.username == ?", (username,))
        user_exist = cursor.fetchone()
        if user_exist:
            return render_template("register.html", error="El username ya esta en uso")

        conn, cursor = get_db_conection()
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/perfil')
    
       






app.run(debug=True)