from flask import Blueprint, render_template, request
import requests

API_KEY = "chave aqui"
BASE_URL = "https://api.themoviedb.org/3"

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    query = request.args.get("query")
    
    url_populares = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=pt-BR&page=1"
    filmes_populares = requests.get(url_populares).json()["results"]
    
    url_em_alta = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=pt-BR&page=1"
    filmes_em_alta = requests.get(url_em_alta).json()["results"]
    
    if query:
        url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language=pt-BR&query={query}"
        filmes = requests.get(url).json()["results"]
        return render_template("index.html", filmes=filmes, 
                                            filmes_populares=filmes_populares, 
                                            filmes_em_alta=filmes_em_alta)
    else:
        return render_template("index.html", filmes=filmes_populares, 
                               filmes_populares=filmes_populares, 
                               filmes_em_alta=filmes_em_alta)

@bp.route("/detalhe/<int:filme_id>")
def detalhe(filme_id):
    url = f"{BASE_URL}/movie/{filme_id}?api_key={API_KEY}&language=pt-BR"
    filme = requests.get(url).json()
    return render_template("detalhe.html", filme=filme)

def init_app(app):
    app.register_blueprint(bp)