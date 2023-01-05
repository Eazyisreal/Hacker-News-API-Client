from django.shortcuts import render
from django.views.generic import ListView
from .models import News

class NewsListView(ListView):
    def get(self, request):
        news_items = News.objects.all().order_by('-item_id')
        context = {'news_items': news_items}
        return render(request, 'news_list.html', context)
