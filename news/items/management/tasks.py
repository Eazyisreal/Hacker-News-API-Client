# from celery import shared_task
# from .utils import sync_news

# @shared_task
# def sync_news_task():
#     sync_news()


# myapp/management/tasks.py

from django.core.management import call_command
from django.utils import timezone
from celery.task import periodic_task

@periodic_task(run_every=timezone.timedelta(minutes=5))
def sync_news():
    # Call the sync_news management command
    call_command('sync_news')
