# from django.shortcuts import render
# from django.views.generic import ListView
# from rest_framework import viewsets
# from .serializers import NewsSerializer
# from .models import News
# from django.core.paginator import Paginator
# import requests
# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsListView(ListView):
#     def get(self, request):
#         type = request.GET.get('type')
#         search = request.GET.get('search')
        
#         # Fetch news items from the API
#         api_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
#         params = {}
#         if type:
#             params['type'] = type
#         if search:
#             params['search'] = search
#         response = requests.get(api_url, params=params)
#         news_items = response.json()
        
#         # Filter and paginate the news items
#         paginator = Paginator(news_items, 5) # Show 5 items per page
#         page = request.GET.get('page')
#         news_items = paginator.get_page(page)
#         context = {'news_items': news_items}
#         return render(request, 'news_list.html', context)



from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import News
from .viewsets import NewsViewSet
    


def news_list(request):
    # Get the search term and type filter values from the request
    search_term = request.GET.get('search')
    item_type = request.GET.get('type')

    if search_term:
        # Filter the news items by the search term
        news_items = News.objects.filter(title__icontains=search_term).order_by('-created_at')
    elif item_type:
        # Filter the news items by the specified type
        news_items = News.objects.filter(type=item_type).order_by('-created_at')
    else:
        # No filters specified, show all news items
        news_items = News.objects.all().order_by('-created_at')

    # Use Paginator to paginate the news items
    paginator = Paginator(news_items, 10)  # Show 10 news items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news_list.html', {'page_obj': page_obj})



def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    children = News.objects.filter(parent=news_item)
    return render(request, 'news_detail.html', {'news_item': news_item, 'children': children})

