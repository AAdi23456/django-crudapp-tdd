from django.urls import path
from . import views

urlpatterns = [
    path("temprature/<str:city>/", views.get_cite, name="get_city"),
    path("addcity/", views.create_city, name="create_city"),
    path("delete/<str:city>/", views.delete_city, name="delete_city"),
    path("update/<str:city>/", views.update_city, name="update_city"),
]
