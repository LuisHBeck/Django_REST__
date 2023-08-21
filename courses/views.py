from rest_framework import generics
from rest_framework.generics import get_object_or_404

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
    
    def get_queryset(self):
        pk = self.kwargs.get('course_pk')
        if pk:
            return self.queryset.filter(course_id=pk)
        return self.queryset.all()
    
    
# List, Update and Delete a specific rating
class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    
    def get_object(self):
        pk_course = self.kwargs.get('course_pk')
        pk_rating = self.kwargs.get('rating_pk')
        if pk_course:
            return get_object_or_404(
                self.get_queryset(), 
                course_id=pk_course,
                pk=pk_rating
            )
        return get_object_or_404(
            self.get_queryset(), 
            pk=pk_rating
        )