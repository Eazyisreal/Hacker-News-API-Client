
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include ('items.urls')),
    
# ]
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from items import viewsets


router = routers.DefaultRouter()
router.register(r'news', viewsets.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('items.urls')),
    path('api/', include(router.urls)),
    # Other URL patterns...
]
