from django.urls import path
from .views import NewsListView, NewsDetailView, NewsByTagListView


app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('tag/<str:tag>/', NewsByTagListView.as_view(), name='news-by-tag'),
]
