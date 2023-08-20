from rest_framework import serializers
from .models import Course, Rating


class RatingSerializers(serializers.Serializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = [
            'id', 
            'name', 
            'email', 
            'course', 
            'comment', 
            'rating'
        ]
        

class CourseSerializer(serializers.Serializer):
    
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'published',
            'active'
        ]