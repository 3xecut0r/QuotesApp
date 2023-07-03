import json

from pymongo import MongoClient


client = MongoClient('mongodb://localhost')

db = client.quotescraper

with open('quotes.json', 'r') as f:
    quotes = json.load(f)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author'][0]})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': author['fullname']
        })
        print('Done')
