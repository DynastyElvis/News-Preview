from flask import render_template 
from . import main 
from ..request import get_news 

"""
__name__ is a special variable that is set to the name of the module in which it is used.

"""
#views

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting news
    news = get_news()
    title = 'Home - Welcome to the best News Highlighter Website Online'
    return render_template('index.html', title = title, articles = news)

    """__name__ is a special variable that is set to the name of the module in which it is used.
    """