from django.contrib import admin

from .models import Course, Rating


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'active']
    ordering = ['id']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'comment', 'rating']
    ordering = ['id']
