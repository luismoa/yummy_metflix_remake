from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import ModelMovieSerializer
from ..models import Movie


class MovieApiView(ViewSet):

    def list(self, request):
        movies = ModelMovieSerializer(Movie.objects.all(), many=True)
        return Response(data=movies.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: int):
        if pk is None:
            return Response(request, status=status.HTTP_400_BAD_REQUEST)

        movie_obj = Movie.objects.filter(id=pk).first()
        if movie_obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie = ModelMovieSerializer(movie_obj)
        return Response(data=movie.data, status=status.HTTP_200_OK)

    def create(self, request):
        movie = ModelMovieSerializer(data=request.POST)
        movie.is_valid(raise_exception=True)
        if movie.is_valid():
            movie_obj = movie.save()
            return self.retrieve(request, pk=movie_obj.id)
        return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        movie_instance = Movie.objects.get(id=pk)
        if movie_instance is not None:
            movie_serializer = ModelMovieSerializer(instance=movie_instance, data=request.data)
            if movie_serializer.is_valid():
                movie_serializer.save()
                serializer_dict = movie_serializer.data
                return Response(serializer_dict, status=status.HTTP_200_OK)
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
