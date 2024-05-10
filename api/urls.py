from rest_framework import routers
from django.urls import path
from .views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
urlpatterns = router.urls
