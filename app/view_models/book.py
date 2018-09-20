#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from app.sipder.yushu import Book


class BookViewModel(object):

    def __init__(self, book_data: str):
        self.title = book_data.get('title')
        self.author = '、'.join(book_data.get('author'))
        self.binding = book_data.get('binding')
        self.publisher = book_data.get('publisher')
        self.image = book_data.get('image')
        self.price = '￥' + book_data.get('price') or ''
        self.isbn = ''
        self.pubdate = book_data.get('pubdate')
        self.summary = book_data.get('summary') or ''
        self.pages = book_data.get('pages')

    @property
    def intro(self):
        return '/'.join(filter(lambda x: x != '', [self.author, self.publisher, self.price]))


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, book: Book, keyword: str):
        self.books = [BookViewModel(book_data) for book_data in book.books]
        self.keyword = keyword
        self.total = book.total


if __name__ == '__main__':
    basename = os.path.basename('/app/models/book.py')
    print(basename)
