import requests
import json

query = input("Enter news query: ")

url = (f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey=94cafaa9b0b14caf9bd024f93a3534de")

print("Fetching news from: ", url)

try:
    response_dict = requests.get(url).json()

    if response_dict['status'] == 'ok':
        articles = response_dict['articles']
        i = 0
        for article in articles:
            i +=1 
            print(f"{i}: Authors: {article['author']}\nTitle: {article['title']}\nDescription: {article['description']}\n")
            print("--------------------------------------------")

except Exception as e:
    print("Some error occured" , e)

