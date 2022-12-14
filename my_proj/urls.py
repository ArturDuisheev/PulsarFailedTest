from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_proj import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('shop.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
