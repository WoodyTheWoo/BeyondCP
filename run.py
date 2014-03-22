# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - run.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import flask

import omdb
import database
import rss


app = flask.Flask(__name__)


@app.route('/')
def index():
    films_list = database.db_list_movies()
    return flask.render_template("index.html", films=films_list)


@app.route('/config')
def config():
    qualities = database.db_get_quality_settings()
    return flask.render_template("config.html", qualities=qualities)


@app.route('/search', methods=['GET'])
def search():
    str_search = flask.request.args['str_search']
    films_list = omdb.omdb_search(str_search)
    return flask.render_template("search.html", films=films_list)


@app.route('/_add_movie_to_db', methods=['GET'])
def add_movie_to_db():
    title = flask.request.args['title']
    year = flask.request.args['year']
    imdb_id = flask.request.args['imdb_id']
    database.db_insert_movie(title, year, imdb_id)
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


@app.route('/_search_for_torrents', methods=['GET'])
def search_for_torrents():
    films = database.db_list_movies()
    quality = database.db_get_quality_settings()

    for film in films:
        rss.search_for_film(quality[1]['rss'], film['title'].replace(':', ''))

    return 'OK'


if __name__ == "__main__":
    try:
        with open("static/other/database.db"):
            print("Database OK")
    except IOError:
        print("Database KO")
        database.db_create_table()

    app.run(host='0.0.0.0', debug=True)