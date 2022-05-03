import unittest # Importing the unittest module
from request import Request # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_request = Request('news','news','news','news','news') # create user object
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Request.requests = []
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_request.id, 'news')
        self.assertEqual(self.new_request.name, 'news')
        self.assertEqual(self.new_request.email, 'news')
        self.assertEqual(self.new_request.username, 'news')
        self.assertEqual(self.new_request.password, 'news')



if __name__ == '__main__':
    unittest.main()