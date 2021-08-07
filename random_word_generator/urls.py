from django.urls import path
from . import views

from django.urls import path
from . import views


urlpatterns = [
path('', views.index),
path('reset', views.reset),
path('score', views.score),
]