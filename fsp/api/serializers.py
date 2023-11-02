from rest_framework import serializers
from .models import Post, Score
    

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['post', 'score']
        
    def validate_score(self, value):
        if value > 5 or value < 0:
            raise serializers.ValidationError('Score must be between 0 and 5.')
        return value
