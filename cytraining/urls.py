from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction_to_cybersecurity, name='introduction_to_cybersecurity'),
    path('intro', views.introduction_to_cybersecurity2, name='introduction_to_cybersecurity'),
]