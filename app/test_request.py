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




if __name__ == '__main__':
    unittest.main()