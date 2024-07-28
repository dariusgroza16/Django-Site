from django.urls import path
from . import views

#Define list of urls
urlpatterns = [
    path('', views.index)
]
