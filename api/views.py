from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from news.models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def like_view(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    news_item.likes += 1
    news_item.save()
    return JsonResponse({'likes': news_item.likes, 'dislikes': news_item.dislikes})


@api_view(['POST'])
@permission_classes([AllowAny])
def dislike_view(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    news_item.dislikes += 1
    news_item.save()
    return JsonResponse({'likes': news_item.likes, 'dislikes': news_item.dislikes})
