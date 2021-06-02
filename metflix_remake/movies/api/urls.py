from django.urls import path
from .views import MovieApiView

urlpatterns = [
    path('', MovieApiView.as_view())
]
