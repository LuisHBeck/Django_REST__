from rest_framework import serializers
from django.db.models import Avg

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
    
    def validate_rating(self, value):
        if value > 0 and value <=5:
            return value
        return serializers.ValidationError('Rating needs to be between 0 and 5')
    

class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # ratings = RatingSerializers(
    #     many=True, 
    #     read_only=True
    # )
    
    # Primary Key Related Field
    # ratings = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )
    

    #HyperLinked Related Field (recommended by RESTFULL design)
    ratings = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='rating-detail'
    )

    ratings_average = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'published',
            'active',
            'ratings',
            'ratings_average'
        )

    def get_ratings_average(self, obj):
        average = obj.ratings.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0
        return round(average*2)/2