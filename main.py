from urllib import parse
import urllib3
import json


## https://developers.themoviedb.org/3/getting-started
## http://www.theimdbapi.org/#

def get_movie(title, year=None):
    request = urllib3.PoolManager()
    params = {'title': title}
    if (year):
        params['year'] = year
    response = request.request('GET', 'http://www.theimdbapi.org/api/find/movie?{}'.format(parse.urlencode(params)))
    data = response.data.decode('UTF-8')
    return json.loads(data)[0]


first_movie = get_movie(input('First film title: '), input('first film year(optional): '))
second_movie = get_movie(input('Second film title: '), input('second film year(optional): '))
matching_cast = [(first, second)
                 for first in first_movie['cast']
                 for second in second_movie['cast']
                 if first['name'] == second['name']]

if (len(matching_cast)):
    print('{} match{}'.format(len(matching_cast), ('es' if len(matching_cast) > 1 else '')), end="\n")
    for first, second in matching_cast:
        print('{} played {} in {} and {} in {}'
              .format(first['name'],
                      first['character'],
                      '{} ({})'.format(first_movie['title'], first_movie['year']),
                      second['character'],
                      '{} ({})'.format(second_movie['title'], second_movie['year'])
                      ),
              end="\n")
else:
    print('No matches between {} and {}'.format('{} ({})'.format(first_movie['title'], first_movie['year']),
                                                '{} ({})'.format(second_movie['title'], second_movie['year'])))
