from flask import  Flask , render_template


app = Flask("__name__") #""" cria uma instnância dessa classe """

@app.route("/")          #""" cria rotas com o decorator """
def home():
    return render_template ("index.html")

@app.route("/quemsomos")          
def quemsomos():
    return render_template ("/quem_somos.html")

@app.route("/contatos")          
def contatos():
    return render_template ("/contatos.html")
