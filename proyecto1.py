from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"autor":"autor 1", "posteo":"Las mejores cervezas se elavoran en..."}, 
    {"autor":"autor 2", "posteo":"La variedad de cervezas mas consumida es.."}
    


    ]

#posts = []

@app.route('/')
def home():
    return render_template("/home.html", posts=posts)


@app.route("/sobre_nosotros")
def sobren_osotros():
    return render_template("sobre_nosotros.html")  

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create_post")
def create_post():
    return render_template("create_post.html")




app.run(debug=True)