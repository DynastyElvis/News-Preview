from app import create_app
from flask_script import Manager,Server

# Creating app instance

'''
This includes running a development server, a customised Python shell, ... from flask_script

'''

app = create_app('development')# creating the app instance
manager = Manager(app) # creating the manager instance
manager.add.command('server',Server) # adding the server command