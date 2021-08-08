import unittest
from app.models import news_detail


class NewsDetailTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_detail class
    '''
# Method to instatiate News_detail class to make self.new_news_detail object.
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_detail= News_detail()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_detail,News_detail))