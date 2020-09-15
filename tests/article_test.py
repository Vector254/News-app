import unittest
from app.models import Articles


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('bbc-news','kevin wright','the epidemic pandemic',
        'coronavirus has become more than just an epidemic, threatening to wipe off the human race',
        'https://www.nytimes.com/2020/08/22/sunday-review/coronavirus-poverty-child-allowance.html',
        'https://static01.nyt.com/images/2020/08/23/opinion/sunday/21Deparle/21Deparle-facebookJumbo.jpg',
        '2018-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_variables(self):
        self.assertEqual(self.new_article.id,'bbc-news')
        self.assertEqual(self.new_article.author,'kevin wright')
        self.assertEqual(self.new_article.title,'the epidemic pandemic')
        self.assertEqual(self.new_article.description,'coronavirus has become more than just an epidemic, threatening to wipe off the human race')
        self.assertEqual(self.new_article.url,'https://www.nytimes.com/2020/08/22/sunday-review/coronavirus-poverty-child-allowance.html')
        self.assertEqual(self.new_article.image,'https://static01.nyt.com/images/2020/08/23/opinion/sunday/21Deparle/21Deparle-facebookJumbo.jpg')
        self.assertEqual(self.new_article.date,'2018-04-11T07:57:16Z')



