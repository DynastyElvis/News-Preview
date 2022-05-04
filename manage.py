from app import create_app
from flask_script import Manager,Server

# Creating app instance

'''
This includes running a development server, a customised Python shell, ... from flask_script

'''

app = create_app('development')# creating the app instance
manager = Manager(app) # creating the manager instance

manager.add_command('server',Server) # adding the server command
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
if __name__ == '__main__':
    manager.run() # running the manager