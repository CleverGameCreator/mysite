from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Все URL блога начинаются с /blog/ и берутся из blog/urls.py
    path('blog/', include('blog.urls', namespace='blog')),
]
