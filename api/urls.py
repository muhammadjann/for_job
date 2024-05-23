from rest_framework import routers
from django.urls import path

from api.views import like_view,dislike_view
from .views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
urlpatterns = [
    path('like/<int:pk>/', like_view, name='like'),
    path('dislike/<int:pk>/', dislike_view, name='like'),
              ]+router.urls
