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


@app.route('/search', methods=['GET'])
def search():
    str_search = flask.request.args['str_search']
    films_list = imdb_search.get_films_list(str_search)
    return flask.render_template("search.html", films=films_list)


@app.route('/_add_movie_to_db', methods=['GET'])
def add_movie_to_db():
    title = flask.request.args['title']
    year = flask.request.args['year']
    imdb_id = flask.request.args['imdb_id']
    database.db_insert_movie(title, year, imdb_id)
    #print title, year, imdb_id
    return flask.jsonify(result=0)


@app.route('/_remove_movie_from_db', methods=['GET'])
def remove_movie_from_db():
    db_id = flask.request.args['id']
    database.db_remove_movie(db_id)
    return flask.redirect("/")


if __name__ == "__main__":
    try:
        with open("database.db"):
            pass
            print "Database OK"
    except IOError:
        print("Database KO")
        database.db_create_table()

    app.run(host='0.0.0.0', debug=True)