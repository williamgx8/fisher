from flask.json import jsonify

from helper import set_key
from run import app
from yushu import Book


@app.route('/book/search/<string:q>/<int:page>')
def search(q: str, page: int):
    query_key = set_key(q)
    result = None
    if query_key == 'isbn':
        result = Book.search_by_isbn(query_key)
    else:
        result = Book.search_by_keyword(query_key)
    return jsonify(result)
