import unittest
from app.models import news_detail


class NewsDetailTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_detail class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_detail= News_detail('')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_detail,News_detail))
        
if __name__ == '__main__':
    unittest.main()  
       