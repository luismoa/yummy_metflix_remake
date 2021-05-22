from django.shortcuts import render, redirect
from .forms import InsertMovieForm
from django.views import View
from .models import Movie
from django.db.models import Count, F, Value


class MovieView(View):
    model = Movie
    model_query = model.objects

    # Template
    movies_template = 'movies.html'

    # Queries
    all_movies = model_query.all()
    movies_count = model_query.count()

    # Forms
    insert_form = InsertMovieForm()

    def get(self, request, *args, **kwargs):
        context = {
            'movie_list': list(self.all_movies),
            'movies_count': self.movies_count,
            'insert_form': self.insert_form,
        }

        return render(request, self.movies_template, context=context)

    def post(self, request, *args, **kwargs):
        insert_form = InsertMovieForm(request.POST)
        if insert_form.is_valid():
            print(insert_form.cleaned_data)
            self.create(insert_form.cleaned_data)
            return redirect(request.path)
        return self.get(request)

    def create(self, data):
        self.model_query.create(
            title=data['title'], running_time=data['running_time']
        )
