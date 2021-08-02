
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    