
import datetime
import requests
from django.core.management.base import BaseCommand
from items.models import News

HACKER_NEWS_API_URL = 'https://hacker-news.firebaseio.com/v0/'

class Command(BaseCommand):
 def handle(self, *args, **options):
    # Get the latest news item IDs from the Hacker News API
    response = requests.get(f'{HACKER_NEWS_API_URL}newstories.json')
    news_item_ids = response.json()

    # Get the details for each news item
    for news_item_id in news_item_ids:
        # Check if the news item already exists in the database
        if not News.objects.filter(id=news_item_id).exists():
            # Get the news item details from the Hacker News API
            response = requests.get(f'{HACKER_NEWS_API_URL}item/{news_item_id}.json')
            news_item_data = response.json()

            # Extract the url from the news item data
            url = None
            if 'url' in news_item_data:
                url = news_item_data['url']
# Convert the value to the correct format before saving it
        created_at = datetime.datetime.fromtimestamp(news_item_data['time'])
        news_item = News(
            id=news_item_data['id'],
            title=news_item_data['title'],
            url=url,
            created_at=created_at,
            type=news_item_data['type'],
        )
        news_item.save()

