import requests

apikey = "94cafaa9b0b14caf9bd024f93a3534de"

def top_headlines():
    try:
        url = (f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apikey}")
        response = requests.get(url).json()

        if response['status'] == 'ok':
            articles = response['articles']
            headlines = []
            for article in articles:
                headlines.append(article['title'])
            
            for i in range(len(headlines)):
                print(i+1,". ",  headlines[i])
    except Exception as e:
        print("Some error occured: ", e)

def business_news():
    try:
        url = (f"https://newsapi.org/v2/top-headlines/sources?category=businessapiKey={apikey}")
        response = requests.get(url).json()
        headlines = []
        if response['status'] == 'ok':
            articles = response['articles']
            for article in articles:
                headlines.append(articles['title'])
            
            for i in range(len(headlines)):
                print(i+1, ".", headlines[i])
    except Exception as e:
        print(e)

top_headlines()
business_news()