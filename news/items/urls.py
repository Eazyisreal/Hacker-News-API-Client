from django.urls import path,include
from rest_framework import routers
from .viewsets import NewsViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', views.news_list),
    path('', views.news_detail),
    path('', include(router.urls)),
]
