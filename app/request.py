import urllib.request,json   
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
        '''
        The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication
        '''
        if get_news_response['articles']:
            news_results_list = get_news_response['articles'] # getting the news results
            news_results = process_results(news_results_list) # processing the news results
            
        return news_results # returning the news results
    
    def process_results(news_list):
        '''
        process resultand transform to object lists
        '''
        news_results = []# creating a list to store the news results
        for news_item in news_list: # iterating through the news list
            title = news_item.get('title')
            description = news_item.get('description')
            urlToImage = news_item.get('urlToImage')
            publishedAt = news_item.get('publishedAt')
            content = news_item.get('content')

        news_object = News(title,description,urlToImage,publishedAt,content) # creating a news object
        news_results.append(news_object)# appending the news object to the news results list
        
    return news_results # returning the news results