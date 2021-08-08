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
     