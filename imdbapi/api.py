import urllib3
from urllib import parse

import json

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': './var/cache/data',
    'cache.lock_dir': './var/cache/lock'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

api_url = 'http://www.theimdbapi.org/api/'


@cache.cache('search_titles', expire=3600)
def search_titles(title):
    request = urllib3.PoolManager()
    params = {'title': title}
    response = request.request('GET', api_url + 'find/movie?{}'.format(parse.urlencode(params)))
    data = response.data.decode('UTF-8')
    return json.loads(data)


@cache.cache('get_matching_cast', expire=3600)
def get_matching_cast(first_movie, second_movie):
    matching_cast = [(first, second)
                     for first in first_movie['cast']
                     for second in second_movie['cast']
                     if first['name'] == second['name']]
    return matching_cast


@cache.cache('get_title', expire=3600)
def get_title(id):
    request = urllib3.PoolManager()
    response = request.request('GET', api_url + 'movie?movie_id=' + id)
    data = response.data.decode('UTF-8')
    return json.loads(data)
