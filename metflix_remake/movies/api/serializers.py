from typing import Dict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Movie


class ModelMovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate(self, movie: Dict[str,str]):
        if not movie.get('title'):
            raise ValidationError('Title is mandatory')
        return movie

    class Meta:
        model = Movie
        # The order here also affects the JSON request order
        fields = [
            'id', 'title', 'nationality',
            'director', 'budget',
            'box_office', 'running_time',
            'production_company', 'year_release',
        ]
