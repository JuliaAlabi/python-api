from flask import render_template
import requests

def init_app(app):
    # Rota Home
    @app.route('/')
    def home():
        return render_template('index.html')

    # Filmes
    @app.route('/filmes')
    def filmes():
        url = "https://swapi.dev/api/films/"
        response = requests.get(url, verify=False)  # ignora SSL
        filmes = response.json()["results"]

        for f in filmes:
            id_filme = f["url"].split("/")[-2]
            f["image"] = f"http://starwars-visualguide.com/assets/img/films/{id_filme}.jpg"

        return render_template("filmes.html", filmes=filmes)

    # Personagens
    @app.route('/personagens')
    def personagens():
        url = "https://swapi.dev/api/people/"
        response = requests.get(url, verify=False)
        personagens = response.json()["results"]

        for p in personagens:
            id_personagem = p["url"].split("/")[-2]
            p["image"] = f"http://starwars-visualguide.com/assets/img/characters/{id_personagem}.jpg"

        return render_template("personagens.html", personagens=personagens)

    # Naves
    @app.route('/naves')
    def naves():
        url = "https://swapi.dev/api/starships/"
        response = requests.get(url, verify=False)
        naves = response.json()["results"]

        for n in naves:
            id_nave = n["url"].split("/")[-2]
            n["image"] = f"http://starwars-visualguide.com/assets/img/starships/{id_nave}.jpg"

        return render_template("naves.html", naves=naves)

    # Planetas
    @app.route('/planetas')
    def planetas():
        url = "https://swapi.dev/api/planets/"
        response = requests.get(url, verify=False)
        planetas = response.json()["results"]

        for p in planetas:
            id_planeta = p["url"].split("/")[-2]
            p["image"] = f"http://starwars-visualguide.com/assets/img/planets/{id_planeta}.jpg"

        return render_template("planetas.html", planetas=planetas)
