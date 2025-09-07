from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from .yasg import urlpatterns as doc_urls
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/', include('hotel.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)