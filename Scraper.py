import requests
from bs4 import BeautifulSoup as bs
import pymongo

more_links = True
page = 1
quotes = []

while(more_links): 
    markup = requests.get(f'http://quotes.toscrape.com/page/{page}').text
    soup = bs(markup, 'html.parser')       
    for item in soup.select('.quote'): 
        quote = {}
        quote['text'] = item.select_one('.text').get_text()
        quote['author'] = item.select_one('.author').get_text()         
        tags = item.select_one('.tags')
        quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
        quotes.append(quote)

    next_link = soup.select_one('.next > a')
    print(f"Page {page} complete")
    
    if(next_link):
        page += 1
    else:
        more_links = False
        
client = # MongoDB access
db = client.db.quotes
try:
    db.insert_many(quotes)
    print(f'inserted {len(quotes)} articles')
except:
    print('an error occurred quotes were not stored to db')