from django.db import models


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name_field = models.CharField(max_length=35)
    nationality = models.CharField(max_length=40)

    class Meta:
        db_table = 'director'


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    nationality = models.CharField(max_length=40)
    production_company = models.CharField(max_length=35)
    year_release = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    budget = models.PositiveBigIntegerField()
    box_office = models.PositiveBigIntegerField()
    running_time = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'movie'


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name_field = models.CharField(max_length=35)
    nationality = models.CharField(max_length=40)
    born = models.DateField()
    sex = models.CharField(max_length=1)

    class Meta:
        db_table = 'actor'


class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role_field = models.CharField(max_length=35)
    is_main_character = models.BooleanField()

    class Meta:
        db_table = 'movie_actor'
