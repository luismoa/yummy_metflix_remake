from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MovieView.as_view(), name='index'),
]
