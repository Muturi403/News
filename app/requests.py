import os
import urllib.request,json
from .models import Source, Article

api_key = None
details_url = None
sources_url = None

def configure_request(app):
  global api_key,sources_url,articles_url
  api_key = app.config['NEWS_API_KEY']
  details_url = app.config['DETAILS_API_BASE_URL']
  sources_url = app.config['SOURCES_API_BASE_URL']
  
def get_source_details(id):
   '''
   Function that gets the json response to our url  request
   '''
   get_news_url = sources_url.format(id,api_key)
   print(get_news_url)
   with urllib.request.urlopen(get_news_url) as url:
     
     get_news_data = url.read()
     get_news_response = json.loads(get_news_data)
     news_results = None
     if get_news_response['details']:
       news_results_list = get_news_response['details']
       news_results = process_results(news_results_list)
       print(news_results)
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
        id = news_item.get('id')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        datePublished = news_item.get('publishedAt')
        pathToImage = news_item.get('urlToImage')
        
        if pathToImage:
            news_object = Article(author,title,description,pathToImage,url,datePublished)
            news_results.append(news_object)
        return news_results    
      
def get_news_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = details_url.format(category,api_key)
    # print(get_news_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)
    return sources_results      
     