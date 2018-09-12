from flask import Blueprint
from flask.json import jsonify

from helper import set_key
from yushu import Book

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/search/<string:q>/<int:page>')
def search(q: str, page: int):
    query_key = set_key(q)
    result = None
    if query_key == 'isbn':
        result = Book.search_by_isbn(query_key)
    else:
        result = Book.search_by_keyword(query_key)
    return jsonify(result)
