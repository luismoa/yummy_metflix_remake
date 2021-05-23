from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Movie


class MovieApiView(APIView):

    def get(self, request):
        movies = [movie for movie in Movie.objects.values_list(named=True)]
        #print(movies)
        return Response(data=movies, status=status.HTTP_200_OK)

    def post(self, request):
        # TODO add another method/way to handle this loading part
        data = {
            'title': request.POST['title'],
            'nationality': request.POST['nationality'],
            'year_release': request.POST['year_release'],
        }
        is_movie_created = self.create(data=data)
        print(f'Movie has been inserted: {is_movie_created}')
        return self.get(request)

    def create(self, data=None):
        is_created = False
        if data is not None:
            self.model_query.create(
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
