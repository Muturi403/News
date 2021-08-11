from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_sources,get_source_articles
from .forms import ReviewForm
from ..models import Review

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    business_source = get_news_sources('business')
    entertainment_source = get_news_sources('entertainment')
    health_source = get_news_sources('health')
    science_source = get_news_sources('science')
    sports_source = get_news_sources('sports')
    technology_source = get_news_sources('technology')

    title = 'Home-News'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, business =  business_source, 
                               technology = technology_source,sports = sports_source,  
                               health = health_source, science = science_source, 
                               entertainment = entertainment_source)

@main.route('/sources')
def articles():
  '''
  view newsdetail page
  '''
  sources=get_news_sources()
  articles= get_source_articles(id)
  
  return render_template('news.html', sources=sources, articles=articles)
