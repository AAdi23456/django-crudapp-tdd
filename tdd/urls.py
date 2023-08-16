from django.urls import path
from . import views

urlpatterns = [
    path('temprature/<str:city>/', views.get_cite, name='get_city'),
   
]
