from httper import Http


class Book(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn_no: str):
        url = Book.isbn_url.format(isbn_no)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword: str, count: int = 15, start: int = 0):
        url = Book.keyword_url.format(keyword, count, start)
        result = Http.get(url)
        return result
