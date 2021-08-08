import unittest
from app.models import news_source


class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_source = News_source('')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source,News_source))


if __name__ == '__main__':
    unittest.main()  