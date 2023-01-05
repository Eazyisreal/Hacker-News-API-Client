from celery import shared_task
from .utils import sync_news

@shared_task
def sync_news_task():
    sync_news()
