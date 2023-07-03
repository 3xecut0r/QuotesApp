import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotescraper.settings')
django.setup()

from quotes.models import Quote, Tag, Author


client = MongoClient('mongodb://localhost')

db = client.quotescraper


authors = db.authors.find()

for author in authors:
    print(author)
