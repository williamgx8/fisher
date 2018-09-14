#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Config(object):
    DEBUG = False
    SECRET_KEY = 'fisher'
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'

    #     custom
    PER_PAGE = 15
