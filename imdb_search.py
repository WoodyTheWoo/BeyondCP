# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - imdb_search.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

from imdb import IMDb


def get_films_list(str_search):
    movie_lst = []

    ia = IMDb()

    movie_list = ia.search_movie(str_search)

    for movie in movie_list:
        movie_dic = {}

        try:
            movie_dic['id'] = int(movie.movieID)
            movie_dic['title'] = movie['title'].replace(' ', '+')
            movie_dic['year'] = int(movie['year'])
            movie_dic['str'] = movie['title'] + ' (' + str(movie['year']) + ')'

            movie_lst.append(movie_dic)
        except KeyError:
            pass

    return movie_lst