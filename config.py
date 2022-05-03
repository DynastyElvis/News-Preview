import os
'''
This module provides the ConfigParser class which implements a 
basic configuration language which provides a structure similar to what's found in 
Microsoft Windows INI files. You can use this to write Python programs which can be customized by end 
users easily.

'''
class Config: # creating a class for the config
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('aa47b48af14d4200bab1105dfc0fe02e')