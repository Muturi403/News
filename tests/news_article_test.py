import unittest
from app.models import news_article


class NewsArticleTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_detail class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_article = News_article('https: // nation.africa/kenya',' Caroline Wafula & Ruth Mbula', 'Live: Mashujaa Day celebrations in Kisii',
                                             'https://nation.africa/kenya/news/hundreds-line-up-to-join-mashujaa-day-celebrations-amid-tight-security-2485374', 'Hundreds line up to join Mashujaa Day celebrations amid tight security',
                                             'https://nation.africa/resource/image/2485466/landscape_ratio16x9/960/540/5122a74e70d1c05a6aea741493cd7859/ee/gusii13.jpg', 'Tuesday, October 20, 2020', 'President Uhuru Kenyatta is expected to grace the important annual celebration later this morning, that follows months of preparations by Kisii County.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,News_article))
        
if __name__ == '__main__':
    unittest.main()  
       
