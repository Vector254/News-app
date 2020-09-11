import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('The Next Web','The cosmic companion','The Moon’s surface is rusting',
        'Dust on the Moon discovered by the Chandrayaan-1 spacecraft orbiting our planet',
        'https://thenextweb.com/syndication/2020/09/11/the-moons-surface-is-rusting-and-earth-may-be-to-blame/','2020-09-11T09:00:22Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()