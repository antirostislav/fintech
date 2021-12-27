from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page),
    path('register/', register_page),
    path('logout/', logout_page)
]
