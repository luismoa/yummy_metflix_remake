from django.db import models


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    _name = models.CharField(max_length=35)
    nationality = models.CharField(max_length=40)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    nationality = models.CharField(max_length=40)
    production_company = models.CharField(max_length=35)
    year_release = models.PositiveIntegerField()
    id_director = models.ForeignKey(Director, on_delete=models.CASCADE)
    budget = models.PositiveBigIntegerField()
    box_office = models.PositiveBigIntegerField()
    running_time = models.PositiveSmallIntegerField()


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    _name = models.CharField(max_length=35)
    nationality = models.CharField(max_length=40)
    born = models.DateField()
    sex = models.CharField(max_length=1)


class MovieActor(models.Model):
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    id_actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    _role = models.CharField(max_length=35)
    is_main_character = models.BooleanField()
