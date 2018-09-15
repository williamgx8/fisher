import json

from flask import request
from flask.json import jsonify

from app.forms.search_forms import SearchForms
from app.view_models.book import BookCollection
from app.web import web
from app.libs.helper import set_key
from app.sipder.yushu import Book


@web.route('/book/search')
def search():
    form = SearchForms(request.args)
    q = form.q.data.strip()
    page = form.page.data

    if form.validate():
        query_key = set_key(q)
        book = Book()
        result = BookCollection()

        if query_key == 'isbn':
            book.search_by_isbn(q)
        else:
            book.search_by_keyword(q, page)

        result.fill(book, q)
        return json.dumps(result, ensure_ascii=False, indent=4, default=lambda o: o.__dict__)

    else:
        return jsonify(form.errors)
