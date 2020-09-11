from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_article, search_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting floods news
  
    title='Home-Welcome to the news app'
    message="Welcome to the News App"
    news=get_news('bbc')
    cnn_news=get_news('cnn')
    
    
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',query=search_news))
    else:
        return render_template('index.html',message=message,news=news,)

@app.route('/news/<query>')
def article(query):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(query)
    title = f'{article.title}'

    return render_template('news.html',title = title,article = article)

@app.route('/search/<query>')
def search(query):
    '''
    View function to display the search results
    '''
    query_list = query.split(" ")
    query_format = "+".join(query_list)
    searched_news = search_news(query_format)
    title = f'search results for {query}'
    return render_template('search.html',news = searched_news)