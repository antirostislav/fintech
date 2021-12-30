from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home_page),

    path('transaction-storage/add/', add_transaction_storage_page),
    path('transaction-storage/get/', get_transaction_storages_page),
    path('transaction/add/', add_transaction_page),

    path('target/add/', add_target_page),
    path('target/get/', get_targets_page),
]
