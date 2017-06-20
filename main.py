from flask import Flask
from flask import request
from flask import render_template

import json

from imdbapi import api

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search_title', methods=['GET'])
def search():
    term = request.args['term']
    titles = api.search_titles(term)
    options = []
    for title in titles:
        options.append(
            {'label': '{} ({})'.format(title['title'], title['year']), 'value': title['imdb_id']}
        )
    return json.dumps(options)


@app.route('/get_title', methods=['GET'])
def get_title():
    imdb_id = request.args['id'];
    title = api.get_title(imdb_id)
    return render_template('title.html', title=title)


@app.route('/compare_titles', methods=['GET'])
def compare_titles():
    first_movie = api.get_title(request.args['first']);
    second_movie = api.get_title(request.args['second']);
    matching_cast = api.get_matching_cast(first_movie, second_movie)
    output_rows = [];
    for first, second in matching_cast:
        row = {'first': first, 'second': second, 'first_movie': first_movie, 'second_movie': second_movie}
        output_rows.append(row)
    return render_template('compare.html', output_rows=output_rows)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
