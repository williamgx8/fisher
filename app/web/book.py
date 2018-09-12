from flask import request
from flask.json import jsonify

from app.forms.search_forms import SearchForms
from app.web import web
from app.libs.helper import set_key
from app.sipder.yushu import Book


@web.route('/book/search')
def search():
    form = SearchForms(request.args)

    if form.validate():
        query_key = set_key(form.q.data.strip())
        result = None
        if query_key == 'isbn':
            result = Book.search_by_isbn(query_key)
        else:
            result = Book.search_by_keyword(query_key, form.page.data)
        return jsonify(result)
    else:
        return jsonify(form.errors)
