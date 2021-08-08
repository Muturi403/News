from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_sources,get_source_details
from .forms import ReviewForm
from ..models import Review

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    
    general = get_news_sources('general')
    business = get_news_sources('business')
    entertainment = get_news_sources('entertainment')
    health = get_news_sources('health')
    science = get_news_sources('science')
    sports = get_news_sources('sports')
    technology = get_news_sources('technology')

    title = 'Home -  News'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, business_sources =  business, 
                               technology_sources = technology,sports_sources = sports,  
                               health_sources = health, science_sources = science, 
                               entertainment_sources = entertainment)

@main.route('/sources/<id>')
def newsDetail(id):
  '''
  view newsdetail page
  '''
  news = get_source_newsdetail(id)
  return render_template('news.html', news = news)