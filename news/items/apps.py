from django.apps import AppConfig

class ItemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'items'


# from django.apps import AppConfig
# from django.conf import settings
# from management.tasks import sync_news


# class ItemsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'items'

#     def ready(self):
#         if not settings.DEBUG:
#             # Sync the news every 5 minutes
#             sync_news.periodic_task(run_every=300)
