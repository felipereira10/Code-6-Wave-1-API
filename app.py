from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def Home():
    return render_template("/index.html")

@app.route("/ferramentas")
def ferramentas():
    return render_template("/ferramentas.html")

@app.route("/pilares")
def pilares():
    return render_template("/pilares.html")

@app.route("/equipe")
def equipe():
    return render_template("/equipe.html")

@app.route("/napratica")
def napratica():
    return render_template("napratica.html")