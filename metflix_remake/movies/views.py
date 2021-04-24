from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views import View

"""def index(response):
    return HttpResponse('First movie view in metflix!')"""


class MovieView(View):
    model = Movie

    # Queries
    all_movies = model.objects.all()

    def get(self, request):
        context = {
            'movie_list': list(self.all_movies)
        }
        return render(request, 'movies.html', context=context)
