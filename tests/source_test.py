import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('bbc-news','BBC news','Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    
    def test_variables(self):
        self.assertEqual(self.new_source.id,'bbc-news')
        self.assertEqual(self.new_source.name,'BBC news')
        self.assertEqual(self.new_source.description,'Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories')
       

