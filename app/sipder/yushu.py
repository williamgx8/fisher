from flask import current_app

from app.libs.httper import Http


class Book(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn_no: str):
        url = Book.isbn_url.format(isbn_no)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword: str, page: int = 1):
        url = Book.keyword_url.format(keyword, current_app.config.get('PER_PAGE'), Book.__get_start(page))
        result = Http.get(url)
        return result

    @classmethod
    def __get_start(cls, page: int = 1):
        return current_app.config.get('PER_PAGE') * (page - 1)
