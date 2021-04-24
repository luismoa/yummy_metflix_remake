"""
This is a sample ("blueprint") queries for movies app
- It will be much easy to make some "copy-paste" and generate new records for testing the database

"""
from movies.models import Director, Movie, Actor, MovieActor

directors = []
movies = []
actors = []
movie_actors = []

directors.append(
    Director.objects.create(name_field='A', nationality='US'),
)
movies.append(
    Movie.objects.create(title='a', nationality='US', production_company='C', year_release=2000, director=directors[0],
                         budget=20, box_office=200, running_time=200)
)
actors.append(
    Actor.objects.create(name_field='Manolo', nationality='ES', born='2000-02-21', sex='f')
)
movie_actors.append(
    MovieActor.objects.create(movie=movies[0], actor=actors[0], role_field='superman', is_main_character=True)
)
