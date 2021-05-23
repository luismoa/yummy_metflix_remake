from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ModelMovieSerializer
from ..models import Movie


class MovieApiView(APIView):

    def get(self, request):
        movies = ModelMovieSerializer(Movie.objects.all(), many=True)
        return Response(data=movies.data, status=status.HTTP_200_OK)

