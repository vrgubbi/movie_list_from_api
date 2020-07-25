import flask
from flask import jsonify, render_template
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/movies', methods=['GET'])
def home():
    movies = requests.get('https://ghibliapi.herokuapp.com/films')
    movies = movies.json()
    movies_list = [(i['title'], i['url']) for i in movies]

    characters = requests.get('https://ghibliapi.herokuapp.com/people')
    characters = characters.json()
    final_list = []
    for movie in movies_list:
        character_list = [character['name'] for character in characters
                          if movie[1] in character['films']]
        final_list.append([movie[0], character_list])
    return render_template('movies.html', final_list=final_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
