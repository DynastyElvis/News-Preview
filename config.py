import os
'''
This module provides the ConfigParser class which implements a 
basic configuration language which provides a structure similar to what's found in 
Microsoft Windows INI files. You can use this to write Python programs which can be customized by end 
users easily.

'''
class Config: # creating a class for the config
    NEWS_API_BASE_URL = 'GET https://newsapi.org/v2/top-headlines?country=us&apiKey=aa47b48af14d4200bab1105dfc0fe02e' # setting the news api base url
    NEWS_API_KEY = os.environ.get('aa47b48af14d4200bab1105dfc0fe02e')
    
    '''
    
    This is an application that will help people who want to get realtime 
    news withouth having to watch TV for the news.

    
    '''
class ProdConfig(Config): # creating a class for the production config
    pass

class DevConfig(Config): # creating a class for the development config
    DEBUG = True # setting the debug to true
    
config_options = { # creating a dictionary for the config options
'development':DevConfig, # setting the development config
'production':ProdConfig # setting the production config
}
