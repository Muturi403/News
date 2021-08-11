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
        self.new_news_source = News_source('https: // nation.africa/kenya/news/hundreds-line-up-to-join-mashujaa-day-celebrations-amid-tight-security-2485374', 'Hundreds line up to join Mashujaa Day celebrations amid tight security','category','en','Kenya')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source,News_source))

# Removed unittest.run() command
# if __name__ == '__main__':
#     unittest.main()  
