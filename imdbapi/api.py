import urllib3
from urllib import parse
import json

## http://www.theimdbapi.org/#

api_url = 'http://www.theimdbapi.org/api/'

def search_titles(title, year=None):
    request = urllib3.PoolManager()
    params = {'title': title}
    if (year):
        params['year'] = year
    response = request.request('GET', api_url + 'find/movie?{}'.format(parse.urlencode(params)))
    data = response.data.decode('UTF-8')
    return json.loads(data)


def get_matching_cast(first_movie, second_movie):
    matching_cast = [(first, second)
                     for first in first_movie['cast']
                     for second in second_movie['cast']
                     if first['name'] == second['name']]
    return matching_cast

def get_title(id):
    request = urllib3.PoolManager()
    response = request.request('GET', api_url + 'movie?movie_id=' + id)
    data = response.data.decode('UTF-8')
    return json.loads(data)