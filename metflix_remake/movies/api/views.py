from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ModelMovieSerializer
from ..models import Movie


class MovieApiView(APIView):

    def get(self, request):
        movies = ModelMovieSerializer(Movie.objects.all(), many=True)
        return Response(data=movies.data, status=status.HTTP_200_OK)

    def post(self, request):
        movie = ModelMovieSerializer(data=request.POST)
        movie.is_valid(raise_exception=True)
        data = {
            'title': movie.validated_data.get('title'),
            'nationality':  movie.validated_data.get('nationality') ,
            'production_company': movie.validated_data.get('production_company'),
            'year_release': movie.validated_data.get('year_release'),
            #'director': movie.validated_data['director'],
            'budget': movie.validated_data.get('budget'),
            'box_office': movie.validated_data.get('box_office'),
            'running_time': movie.validated_data.get('running_time'),
        }
        self.create(data=data)
        return self.get(request)

    def create(self, data=None):
        is_created = False
        if data is not None:
            Movie.objects.create(
                title=data.get('title', None),
                nationality=data.get('nationality', None),
                production_company=data.get('production_company', None),
                year_release=data.get('year_release', None),
                director=data.get('director', None),
                budget=data.get('budget', None),
                box_office=data.get('box_office', None),
                running_time=data.get('running_time', None)
            )
            is_created = True
        return is_created
