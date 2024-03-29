from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CoursesAPIView, 
    CourseAPIView, 
    CourseViewSet,
    RatingsAPIView, 
    RatingAPIView,
    RatingViewSet
)


router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    # COURSES
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/ratings/', RatingsAPIView.as_view(), name='courses_ratings'),
    path('courses/<int:course_pk>/ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='course_rating'),
    
    # RATINGS
    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='rating'),
]