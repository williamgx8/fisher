from flask import current_app

from app.libs.httper import Http


class Book(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __single(self, book_data: dict):
        if book_data:
            self.total = 1
            self.books.append(book_data.get('books'))

    def __collections(self, book_data: dict):
        if book_data:
            self.total = book_data.get('total')
            self.books = book_data.get('books')

    def search_by_isbn(self, isbn_no: str):
        url = Book.isbn_url.format(isbn_no)
        result = Http.get(url)
        self.__single(result)

    def search_by_keyword(self, keyword: str, page: int = 1):
        url = self.keyword_url.format(keyword, current_app.config.get('PER_PAGE'), Book.__get_start(page))
        result = Http.get(url)
        self.__collections(result)

    @classmethod
    def __get_start(cls, page: int = 1):
        return current_app.config.get('PER_PAGE') * (page - 1)
