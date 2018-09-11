#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    @app.route('/')
    def index():
        return 'hello world'


    app.run(host='0.0.0.0', debug=Config.DEBUG)
