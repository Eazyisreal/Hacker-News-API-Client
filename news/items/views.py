from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.core.paginator import Paginator
import requests

class NewsListView(ListView):
    def get(self, request):
        type = request.GET.get('type')
        search = request.GET.get('search')
        
        # Fetch news items from the API
        api_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        params = {}
        if type:
            params['type'] = type
        if search:
            params['search'] = search
        response = requests.get(api_url, params=params)
        news_items = response.json()
        
        # Filter and paginate the news items
        paginator = Paginator(news_items, 5) # Show 5 items per page
        page = request.GET.get('page')
        news_items = paginator.get_page(page)
        context = {'news_items': news_items}
        return render(request, 'news_list.html', context)



    
