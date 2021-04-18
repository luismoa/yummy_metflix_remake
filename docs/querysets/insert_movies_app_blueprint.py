"""
This is a sample ("blueprint") queries for movies app
- It will be much easy to make some "copy-paste" and generate new records for testing the database

"""
from movies.models import Director, Movie, Actor, MovieActor

# I could use a dictionary, then it will be easily to find which position is a movie(by title) or other thing.
# Then when we add a new record to the dictionary we just need (when a FK) to select dictionary key value instead of a position
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

actors.append(
    Actor.objects.create(name_field='Manolo', nationality='ES', born='2000-02-21', sex='f')
)

movie_actors.append(
    MovieActor.objects.create(movie=movies[0], actor=actors[0], role_field='superman', is_main_character=True)
)

# With a loop make each INSERT query and print out "new actor named added to ..." for example
# Add some functions or use a class to arrange this blueprint
