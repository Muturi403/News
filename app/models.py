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
class Details:
    '''
    Details class to define the details object
    '''
    def _init_(self, author, title, description, pathtoImage, url, datePublished):
        self.author = author
        self.title = title
        self.description = description
        self.pathToImage = pathToImage
        self.url = url
        self.datePublished = datePublished
    
    def save_details(self):
        details.all_details.append(self)  
        
class Review:
  
		all_reviews = []
  
		def _init_(self,source,title,urlToImage,review):
				self.source = source
				self.title = title
				self.urlToImage = urlToImage
				self.review = review
    
    '''
    method that appends the review object to a class variable all reviews
    that's an empty list
    '''
    def save_review(self):
      Review.all_reviews.append(self)
      
      
      @classmethod
      def clear_reviews(cls):
        Review.all_reviews.clear()