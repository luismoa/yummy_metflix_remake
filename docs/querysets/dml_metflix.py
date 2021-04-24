"""
    For now this dml (or django script) it will be only available in django shell
    It will be interesting to make a script that makes all these inserts.
"""
from movies.models import Director, Movie, Actor, MovieActor

# TODO: Automate with a resource json and a script reading and inserting data

directors = [
    Director.objects.create(name_field='Peter Jackson', nationality='NZ'),
    Director.objects.create(name_field='Joe Johnston', nationality='US'),
    Director.objects.create(name_field='David Twohy', nationality='US'),
]
movies = [
    Movie.objects.create(
        title='The Lord of the Rings: The Fellowship of the Ring', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2001, director=directors[0],
        budget=93000000, box_office=888300000, running_time=178
    ),
    Movie.objects.create(
        title='The Lord of the Rings: The Fellowship of the Ring (Extended)', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2002, director=directors[0],
        budget=93000000, box_office=888300000, running_time=228
    ),
    Movie.objects.create(
        title='The Lord of the Rings: The Two Towers', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2002, director=directors[0],
        budget=94000000, box_office=951200000, running_time=179
    ),
    Movie.objects.create(
        title='The Lord of the Rings: The Two Towers (Extended)', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2003, director=directors[0],
        budget=94000000, box_office=951200000, running_time=226
    ),
    Movie.objects.create(
        title='The Lord of the Rings: The Return of the King', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2003, director=directors[0],
        budget=94000000, box_office=1142000000, running_time=201
    ),
    Movie.objects.create(
        title='The Lord of the Rings: The Return of the King (Extended)', nationality='US,NZ',
        production_company='New Line Cinema', year_release=2004, director=directors[0],
        budget=94000000, box_office=1142000000, running_time=251
    ),
    Movie.objects.create(
        title='Captian America: The First Avenger', nationality='US',
        production_company='Marvel Studios', year_release=2011, director=directors[1],
        budget=216600000, box_office=370600000, running_time=124
    ),
    Movie.objects.create(
        title='The Chronicles of RiddicK', nationality='US',
        production_company='Radar Pictures', year_release=2004, director=directors[2],
        budget=120000000, box_office=115800000, running_time=119
    ),
]
actors = [
    Actor.objects.create(name_field='Elijah Wood', nationality='US', born='1981-01-28', sex='m'),
    Actor.objects.create(name_field='Sir Ian Murray McKellen', nationality='UK', born='1939-05-25', sex='m'),
    Actor.objects.create(name_field='Viggo Peter Mortensen Jr.', nationality='US', born='1958-10-20', sex='m'),
    Actor.objects.create(name_field='Christ Evans', nationality='US', born='1981-06-13', sex='m'),
    Actor.objects.create(name_field='Mark Sinclair (Vin Diesel)', nationality='US', born='1967-07-18', sex='m'),
]

movie_actors = [
    MovieActor.objects.create(movie=movies[0], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[0], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[0], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[1], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[1], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[1], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[2], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[2], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[2], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[3], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[3], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[3], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[4], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[4], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[4], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[5], actor=actors[0], role_field='Frodo Baggings', is_main_character=True),
    MovieActor.objects.create(movie=movies[5], actor=actors[1], role_field='Gandalf the Grey', is_main_character=True),
    MovieActor.objects.create(movie=movies[5], actor=actors[2], role_field='Aragorn "Strider', is_main_character=True),

    MovieActor.objects.create(movie=movies[6], actor=actors[3], role_field='Steve Rogers (Captian America)', is_main_character=True),

    MovieActor.objects.create(movie=movies[7], actor=actors[4], role_field='Richard B. Riddick', is_main_character=True),
]
movies_insert_list = [
    # The order matters here
    directors,
    movies,
    actors,
    movie_actors
]


def insert():
    for movies_data in movies_insert_list:
        for insert in movies_data:
            insert
