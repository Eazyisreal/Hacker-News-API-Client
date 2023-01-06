
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
    paginator = Paginator(news_items, 5)  # Show 5 news items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news_list.html', {'page_obj': page_obj})



def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    children = News.objects.filter(parent=news_item)
    return render(request, 'news_detail.html', {'news_item': news_item, 'children': children})

