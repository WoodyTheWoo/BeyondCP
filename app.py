# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - app.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import flask

import omdb
import database


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html", films=database.db_list_movies())


@app.route('/config')
def config():
    return flask.render_template("config.html", qualities=database.db_get_quality_settings())


@app.route('/search', methods=['GET'])
def search():
    str_search = flask.request.args['str_search']

    return flask.render_template("search.html", films=omdb.omdb_search(str_search))


@app.route('/_add_movie_to_db', methods=['GET'])
def add_movie_to_db():
    title = flask.request.args['title']
    year = flask.request.args['year']
    imdb_id = flask.request.args['imdb_id']
    database.db_insert_movie(title, year, imdb_id)
    # TODO Thread to add more infos in db (poster, plot, ...)

    return "Movie inserted in database"


@app.route('/_remove_movie_from_db', methods=['GET'])
def remove_movie_from_db():
    db_id = flask.request.args['id']
    database.db_remove_movie(db_id)

    return flask.redirect("/")


@app.route('/_config_done', methods=['POST'])
def config_done():
    quality_settings = flask.request.get_json(force=True)

    for quality in quality_settings:
        quality_title = quality['title']
        quality_rss = quality['rss']

        database.db_insert_quality(quality_title, quality_rss)

    return "Quality saved"


def run(host, debug):
    host = host or '127.0.0.1'
    debug = debug or False

    app.run(host=host, debug=debug)

    # TODO App settings page (beyondhd key, quality wanted, ...)
    # TODO Edit db
    # TODO Quality settings with each movies added