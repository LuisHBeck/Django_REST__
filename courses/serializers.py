from rest_framework import serializers
from .models import Course, Rating


class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'id', 
            'name', 
            'email', 
            'course', 
            'comment', 
            'rating'
        )
        

class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # ratings = RatingSerializers(
    #     many=True, 
    #     read_only=True
    # )
    
    # Primary Key Related Field
    ratings = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )
    
    #HyperLinked Related Field (recommended by RESTFULL design)
    # ratings = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True, 
    #     view_name='rating-detail'
    # )
    
    
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'published',
            'active',
            'ratings'
        )