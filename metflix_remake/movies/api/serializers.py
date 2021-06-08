from rest_framework import serializers
from ..models import Movie, Director


class ModelDirectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name_field = serializers.CharField(max_length=60, required=False)
    nationality = serializers.CharField(required=False)

    class Meta:
        model = Director
        fields = [
            'id', 'name_field', 'nationality',
        ]


class ModelMovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60, required=False)
    nationality = serializers.CharField(required=False)
    production_company = serializers.CharField(max_length=35, required=False)
    year_release = serializers.IntegerField(required=False)
    director = ModelDirectorSerializer(many=False,required=False)
    budget = serializers.IntegerField(required=False)
    box_office = serializers.IntegerField(required=False)
    running_time = serializers.IntegerField(required=False)

    class Meta:
        model = Movie
        # The order here also affects the JSON request order
        fields = [
            'id', 'title', 'nationality',
            'director', 'budget',
            'box_office', 'running_time',
            'production_company', 'year_release',
        ]
