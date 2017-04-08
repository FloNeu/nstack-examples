#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.GetIMDBScore Service
"""
from imdbpie import Imdb

import nstack

class Service(nstack.BaseService):
    def __init__(self):
        self.imdb = Imdb()
        # self.imdb = Imdb(anonymize=True) # to proxy requests

    # Title -> MovieRecord
    def getIMDBScore(self, title):
        x = self.imdb.search_for_title(title)[0]['imdb_id']
        y = self.imdb.get_title_by_id(x)
        return (title, y.rating)

