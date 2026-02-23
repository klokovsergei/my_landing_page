from flask import Blueprint, abort, render_template
from .services import get_article_by_id

blog_bp = Blueprint(
    'blog',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@blog_bp.route('/<int:article_id>')
def article_page(article_id: int):
    article = get_article_by_id(article_id)
    if not article:
        abort(404)
    return render_template('blog/article.html', article=article)
