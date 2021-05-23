from django.urls import path
from . import views
from .api.views import MovieApiView

urlpatterns = [
    path('', views.MovieView.as_view(), name='index'),
    path('api/', MovieApiView.as_view())
]
