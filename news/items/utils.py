# import requests
# from .models import News

# def sync_news():
#     # fetch the latest 100 items from the Hacker News API
#     response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
#     item_ids = response.json()[:100]

#     for item_id in item_ids:
#         # fetch the item details from the Hacker News API
#         item_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
#         item = item_response.json()

#         # create a News object and save it to the database
#         news_item, created = News.objects.update_or_create(
#             item_id=item['id'],
#             defaults={
#                 'item_type': item['type'],
#                 'title': item['title'],
#                 'body': item.get('text', ''),
#                 'url': item.get('url', ''),
#             }
#         )


import datetime

def parse_datetime(value):
    if isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    else:
        raise ValueError('Invalid datetime value')
