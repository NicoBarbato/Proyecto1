import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
name = "Nicolas Barbato"

def get_db_conection():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

posts = [
    {"id":1, "autor":"autor 1", "titulo":"Mejores Cervezas","posteo":"Las mejores cervezas se elavoran en..."}, 
    {"id":2, "autor":"autor 2", "titulo":"Mejores Variedades","posteo":"La variedad de cervezas mas consumida es.."},
    {"id":3, "autor":"autor 3", "titulo":"Mejores Marcas","posteo":"ashfalknfaksfnakjdnasda.."},
    {"id":4, "autor":"autor 4", "titulo":"Tipos de copas","posteo":"kjdhfkjasnd,and,mnsd.."},
    {"id":5, "autor":"autor 5", "titulo":"Paises mas consumidores","posteo":"sdgsdgasdfsdfsdfgsdg.."},

    ]
users = [
    {"id":1, "username": "nbarbato", "password":"12345"},
    {"id":1, "username": "nicob", "password":"12345"}
    ]

#posts = []

@app.route('/')
def home():
    busqueda = request.args.get('search')
    if busqueda:
         list_post = []
         for post in posts:
             if busqueda.lower() in post['titulo'].lower():
                 list_post.append(post)
         return render_template("home.html", posts=list_post)
    else:
         return render_template("home.html", posts=posts)
    


@app.route("/sobre_nosotros")
def sobren_osotros():
    return render_template("sobre_nosotros.html")  

@app.route("/login", methods=["GET", "POST"])
def login():
     if request.method == "GET":
        return render_template("login.html")
     elif request.method == "POST":
         for user in users:
            if user['username'] == request.form["username"] and user['password'] == request.form["password"]:
             return redirect('/perfil')

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")
    

@app.route("/create_post", methods=["GET","POST"])
def create_post():
        if request.method == "GET":
            return render_template("create_post.html")
        elif request.method == "POST":
            autor = request.form["autor"]
            titulo = request.form["titulo"]
            posteo = request.form["posteo"]
            if autor and titulo and posteo:
                    conn = get_db_conection()
                    conn.execute("INSERT INTO posts (autor, titulo, posteo) VALUES (?,?,?)", (autor, titulo, posteo))
                    conn.commit()
                    conn.close()
            return redirect('/')
            


@app.route("/post", methods=["GET", "POST"])
def post():
    return render_template("post.html")

@app.route("/post/<int:id>")
def busqueda(id):
     #list_post = []
     for post in posts:
         if post["id"] == id: 
             #list_post.append(post)

          return render_template("post.html", post=post)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn, cursor = get_db_conection()
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')
       #     user_exist = list(filter(lambda user: user['username'] == request.form["username"], users))
        #    if user_exist:
         #       return render_template("register.html", error="El username ya existe")
          #  new_id = users[-1]["id"] + 1
           # new_user = {"id": new_id, "username": request.form["username"], "password":  request.form["password"]}
            #users.append(new_user)
            #return redirect('/perfil')



app.run(debug=True)