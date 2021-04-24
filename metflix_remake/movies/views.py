from django.shortcuts import render
from .models import Movie
from django.views import View


class MovieView(View):
    model = Movie

    # Queries
    all_movies = model.objects.all()
    movies_count = model.objects.count()

    def get(self, request):
        context = {
            'movie_list': list(self.all_movies),
            'movies_count': self.movies_count
        }
        return render(request, 'movies.html', context=context)
