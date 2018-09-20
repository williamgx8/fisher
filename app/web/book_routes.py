from flask import request, flash, render_template

from app.forms.search_forms import SearchForms
from app.libs.helper import set_key
from app.sipder.yushu import Book
from app.view_models.book import BookCollection
from app.web import web


@web.route('/book/search')
def search():
    form = SearchForms(request.args)
    q = form.q.data.strip()
    page = form.page.data
    result = BookCollection()

    if form.validate():
        query_key = set_key(q)
        book = Book()

        if query_key == 'isbn':
            book.search_by_isbn(q)
        else:
            book.search_by_keyword(q, page)

        result.fill(book, q)

    else:
        flash('搜索的关键字不符合要求，请重新搜索')

    return render_template('search_result.html', books=result)


@web.route('/book/<string:isbn>/detail')
def book_detail(isbn):
    pass
