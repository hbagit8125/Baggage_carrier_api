from django.urls import path
from . import views

urlpatterns = [
    path('carrier/', views.carrier_data, name='carrier'),
]
