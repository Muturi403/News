class Source:
    ''' 
    Sources class to define the news source objects 
    '''
    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        
class Article:
    '''
    Articles class to define the articles object
    '''
    def _init_(self, author, title, description, pathtoImage, url, datePublished):
        self.author = author
        self.title = title
        self.description = description
        self.pathToImage = pathToImage
        self.url = url
        self.datePublished = datePublished
    
    def save_article(self):
        article.all_articles.append(self)  