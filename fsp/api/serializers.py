from rest_framework import serializers
from .models import Post, User


def score_validator(value):
    if value > 5 or value < 0:
        raise serializers.ValidationError('Score must be between 0 and 5.')

def post_validator(value):
    if not Post.objects.filter(id=value).exists():
        raise serializers.ValidationError('No such post exists.')


class ScoreSerializer(serializers.Serializer):
    score = serializers.IntegerField(validators=[score_validator])
    post = serializers.IntegerField(validators=[post_validator])
    
