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