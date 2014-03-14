# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - imdb_search.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

from imdb import IMDb


def get_rambo(input):
    movie_lst = []

    ia = IMDb(accessSystem='mobile')

    movie_list = ia.search_movie(input)

    for i in movie_list:
        movie_lst.append(i['year'])

    return movie_lst