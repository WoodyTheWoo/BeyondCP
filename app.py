# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - app.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import flask

import imdb_search
import database


app = flask.Flask(__name__)


@app.route('/')
def index():
    films_list = database.db_list_movies()
    return flask.render_template("index.html", films=films_list)


@app.route('/search', methods=['GET', 'POST'])
def search():
    str_search = flask.request.form['str_search']
    films_list = imdb_search.get_films_list(str_search)
    return flask.render_template("search.html", films=films_list)


if __name__ == "__main__":
    try:
        with open("database.db"):
            pass
            print "Database OK"
    except IOError:
        print("Database KO")
        database.db_create_table()

    app.run(host='0.0.0.0', debug=True)