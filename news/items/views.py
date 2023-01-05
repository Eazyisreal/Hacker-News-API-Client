from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.core.paginator import Paginator

class NewsListView(ListView):
    def get(self, request):
        type = request.GET.get('type')
        search = request.GET.get('search')
        news_items = News.objects.all()
        if type:
            news_items = news_items.filter(item_type=type)
        if search:
            news_items = news_items.filter(title__icontains=search)
        news_items = news_items.order_by('-item_id')
        paginator = Paginator(news_items, 10) # Show 10 items per page
        page = request.GET.get('page')
        news_items = paginator.get_page(page)
        context = {'news_items': news_items}
        return render(request, 'news_list.html', context)
