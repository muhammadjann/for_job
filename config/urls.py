from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from config.swagger import schema_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('news.urls')),
                  path('api/v1/', include('api.urls')),
                  path(
                      "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
                  ),
                  path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name=" "),
                  path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
