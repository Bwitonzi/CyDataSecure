from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage1', views.homepage1, name='home'),
    path('homepage2', views.homepage2, name='home'),
]