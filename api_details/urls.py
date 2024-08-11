from django.urls import path
from .views import get_annual_data, get_all_data

urlpatterns = [
    path('data', get_annual_data, name='get_annual_data'),
    path('alldata', get_all_data, name='get_all_data'),
]