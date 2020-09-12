from app import app
import urllib.request,json
from .models import article

Article=article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        author= news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        published_at = news_item.get('publishedAt')

        
        news_object = Article(source,author,title,description,url,published_at)
        news_results.append(news_object)

    return news_results

def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = base_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object

def process_articles(articles_list):
	'''
	'''
	articles_object = []
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	
		

		

		

	return articles_object

def search_news(query):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results