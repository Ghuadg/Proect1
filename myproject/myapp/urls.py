from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('videocard', views.videocard),
    path('cpu', views.cpu)
]
