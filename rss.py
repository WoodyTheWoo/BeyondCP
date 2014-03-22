# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - rss.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

import feedparser


def search_for_film(quality_rss, film_title):
    rss = feedparser.parse(quality_rss)

    for film in rss.entries:
        if film_title in film['title']:
            url = film['link']
            local_filename = film_title + '.torrent'
            # r = requests.get(url, stream=True)
            #
            # with open(local_filename, 'wb') as file:
            #     for chunk in r.iter_content(chunk_size=1024):
            #         if chunk:
            #             file.write(chunk)
            #             file.flush()

            print(url, local_filename)