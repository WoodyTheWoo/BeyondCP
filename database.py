# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - database.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import sqlite3


DATABASE_PATH = 'static/other/database.db'


def db_create_table():
    db = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS
                          movies_wanted(id INTEGER PRIMARY KEY,
                                        title TEXT,
                                        year INTEGER,
                                        imdb_id INTEGER,
                                        imdb_poster_link TEXT)''')

        db.commit()

        cursor.execute('''CREATE TABLE IF NOT EXISTS
                          quality_settings( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            rss_link TEXT)''')

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def db_insert_movie(movie_title, movie_year, movie_id):
    db = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = db.cursor()

        cursor.execute('''INSERT INTO movies_wanted (id, title, year, imdb_id)
                          VALUES(NULL, ?, ?, ?)''', (movie_title, movie_year, movie_id))

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def db_remove_movie(db_id):
    db = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = db.cursor()

        cursor.execute('''DELETE FROM movies_wanted WHERE id=?''', db_id)

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def db_list_movies():
    movie_lst = []

    db = sqlite3.connect(DATABASE_PATH)
    cursor = db.cursor()

    cursor.execute('''SELECT title, year, imdb_id, id FROM movies_wanted''')

    for row in cursor:
        #print("{0} ({1}) (id: {2})".format(row[0], row[1], row[2]))
        movie_dic = {}
        movie_dic['id'] = row[2]
        movie_dic['str'] = row[0] + ' (' + str(row[1]) + ')'
        movie_dic['db_id'] = row[3]
        movie_dic['title'] = row[0]
        movie_lst.append(movie_dic)

    return movie_lst


def db_get_quality_settings():
    quality_lst = []

    db = sqlite3.connect(DATABASE_PATH)
    cursor = db.cursor()

    cursor.execute('''SELECT title, rss_link FROM quality_settings''')

    for row in cursor:
        #print("{0} {1}".format(row[0], row[1]))
        quality_dic = {}
        quality_dic['title'] = row[0]
        quality_dic['rss'] = row[1]
        quality_lst.append(quality_dic)

    return quality_lst


def db_insert_quality(quality_title, quality_rss):
    db = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = db.cursor()

        cursor.execute('''INSERT INTO quality_settings (id, title, rss_link)
                          VALUES(NULL, ?, ?)''', (quality_title, quality_rss))

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()