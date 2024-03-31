from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .swagger import urlpatterns as swagger_patterns
from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/task1/", include("apps.task1.urls")),
    path("api/v1/task2/", include("apps.task2.urls")),
    path("api/v1/task3/", include("apps.task3.urls")),
]
urlpatterns += swagger_patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
