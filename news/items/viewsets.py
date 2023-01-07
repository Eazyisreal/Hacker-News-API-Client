
from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    
    
@api_view(['PATCH'])
def update_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    serializer = NewsSerializer(news, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
