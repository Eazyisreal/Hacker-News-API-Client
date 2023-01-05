from django.urls import path,include
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view()),
]
