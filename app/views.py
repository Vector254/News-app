from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting floods news
    floods_news=get_news('floods')
    tech_news=get_news('technology')
    title='Home-Welcome to the news app'
    message="Welcome to the News App"
    return render_template('index.html',message=message, floods=floods_news, tech=tech_news)

@app.route('/top-headlines/<country>')
def movie(country):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',country=country)