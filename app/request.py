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

def get_news(): # getting the news
    get_news_url = base_url.format(api_key) # getting the news url

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
        return news_results