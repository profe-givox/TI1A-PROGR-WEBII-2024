

from polls import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='public'),
    path('index', views.index, name='index'),
]
