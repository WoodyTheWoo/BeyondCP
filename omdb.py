# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - omdb.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import json

import six.moves.urllib


OMDB_API_SEARCH_URL = "http://www.omdbapi.com/?r=json&s=%s"
OMDB_API_ID_URL = "http://www.omdbapi.com/?r=json&i=%s"


def omdb_search(title):
    movie_lst = []

    title = title.encode("utf-8")
    url = OMDB_API_SEARCH_URL % six.moves.urllib.parse.quote(title)
    data = six.moves.urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(data)

    movie_list = data.get("Search", [])

    for movie in movie_list:
        movie_dic = {}

        if movie['Type'] == 'movie':
            movie_dic['id'] = int(movie['imdbID'].replace('tt', ''))
            movie_dic['title'] = str(movie['Title'])
            movie_dic['year'] = int(movie['Year'])

            movie_lst.append(movie_dic)

    return movie_lst


def omdb_get_poster_url(imdb_id):
    url = OMDB_API_ID_URL % six.moves.urllib.parse.quote('tt' + str(imdb_id))
    data = six.moves.urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(data)

    return data.get('Poster', [])


    # TODO Get plot method