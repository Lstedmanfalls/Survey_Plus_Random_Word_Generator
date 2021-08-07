from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('show_page', views.show_page),
path('results', views.results),
]