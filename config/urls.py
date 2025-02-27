from django.contrib import admin
from django.urls import path, include
from accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('social_django.urls', namespace='social')),  # Social Auth URLs
]
