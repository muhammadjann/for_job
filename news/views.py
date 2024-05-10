from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Tag


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        News.objects.filter(pk=pk).update(views_count=F('views_count') + 1)
        return News.objects.prefetch_related('tags').filter(pk=pk)


class NewsByTagListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag')
        queryset = News.objects.filter(tags__name__in=[tag_name])
        return queryset
