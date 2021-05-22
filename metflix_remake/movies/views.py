from django.shortcuts import render, redirect
from .forms import InsertMovieForm
from django.views import View
from .models import Movie


class MovieView(View):
    model = Movie
    model_query = model.objects

    # Template
    movies_template = 'movies.html'

    # Forms
    insert_form = InsertMovieForm()

    def get(self, request, *args, **kwargs):
        context = {
            'movie_list': self.get_queryset(),
            'movies_count': self.model_query.count(),
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

    def get_queryset(self):
        return list(self.model_query.all())


