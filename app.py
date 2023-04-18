from flask import  Flask , render_template


app = Flask("__name__") #""" cria uma instnância dessa classe """

@app.route("/")          #""" cria rotas com o decorator """
def home():
    return render_template ("index.html")

@app.route("/Pilares")          
def pilares():
    return render_template ("/pilares.html")

@app.route("/Equipe")          
def equipe():
    return render_template ("/equipe.html")

@app.route("/Downloads")          
def download():
    return render_template ("/download.html")

@app.route("/Ferramentas")          
def ferramenta():
    return render_template ("/ferramentas.html")

@app.route("/Oqueé")          
def oqueé():
    return render_template ("/indez.html #oqueé")