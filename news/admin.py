from django.contrib import admin
from news.models import News, Tag


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    ordering = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(News, NewsAdmin)
