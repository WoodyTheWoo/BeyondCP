# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - app.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

from flask import Flask, render_template, request

import imdb_search


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def search():
    s = request.form['email']
    films_db = imdb_search.get_rambo(s)
    return render_template("search.html", films=films_db)


if __name__ == "__main__":
    app.run(debug=True)