# from celery import shared_task
# from .utils import sync_news

# @shared_task
# def sync_news_task():
#     sync_news()


from django.utils import timezone
import requests
# from .models import News

def sync_news():
    # Fetch the latest news items from the Hacker News API
    api_response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json')
    new_item_ids = api_response.json()

    # Iterate over the new item IDs and create a NewsItem object for each one
    for item_id in new_item_ids:
        # Fetch the item data from the API
        item_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
        item_data = item_response.json()

        # Create a NewsItem object with the item data
        # news_item = News(
        #     title=item_data['title'],
        #     url=item_data['url'],
        #     created_at=timezone.datetime.fromtimestamp(item_data['time']),
        #     type=item_data['type'],
        # )
        # news_item.save()

