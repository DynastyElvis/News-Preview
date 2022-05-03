import urllib.request,json   #
from .model import News
"""

Loading JSON object in Python using urllib.request and json 
    
"""     
api_key = None # Enter your API key here
base_url = None # getting the ews base url

def configure_request(app): # configuring the request
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    
    """_request_url is a function that returns the url for the news summary request
    """
