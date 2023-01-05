from celery.schedules import crontab
from celery.decorators import periodic_task

@periodic_task(run_every=crontab(minute='*/5'))
def sync_news():
    sync_news_task.delay()
