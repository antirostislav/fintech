from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home', home_page)
]
