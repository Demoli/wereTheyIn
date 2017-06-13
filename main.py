from flask import Flask
from flask import request
from flask import render_template
import os
from imdbapi import api
import json

# if (len(matching_cast)):
#     print('{} match{}'.format(len(matching_cast), ('es' if len(matching_cast) > 1 else '')), end="\n")
#     for first, second in matching_cast:
#         print('{} played {} in {} and {} in {}'
#               .format(first['name'],
#                       first['character'],
#                       '{} ({})'.format(first_movie['title'], first_movie['year']),
#                       second['character'],
#                       '{} ({})'.format(second_movie['title'], second_movie['year'])
#                       ),
#               end="\n")
# else:
#     print('No matches between {} and {}'.format('{} ({})'.format(first_movie['title'], first_movie['year']),
#                                                 '{} ({})'.format(second_movie['title'], second_movie['year'])))

app = Flask(__name__)

def get_template_path(template):
    return os.getcwd() + '/templates/' + template

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/search_title', methods=['GET'])
def search():
    term = request.args['term']
    titles = api.search_titles(term)
    # titles = [{'label':'Lorem','value':'Lorem'}]
    # return json.dumps(titles);
    options = []
    for title in titles:
        options.append(
            {'label':'{} ({})'.format(title['title'], title['year']),'value': title['imdb_id']}
        )

    return json.dumps(options)


if __name__ == '__main__':
    app.run(debug=True)