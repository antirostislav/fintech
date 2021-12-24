from django.urls import path

from .views import *

urlpatterns = [
    path('target/add/', add_target_page),
    path('target/get/', get_targets_page),
]
