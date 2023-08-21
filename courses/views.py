from rest_framework import generics

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializers

# List all courses and create new one
class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
# List, Update and Delete a specific course 
class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
# List all ratings and create new one 
class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    
    
# List, Update and Delete a specific rating
class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    