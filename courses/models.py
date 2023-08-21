from django.db import models

class Base(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=50)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']

    def __str__(self) -> str:
        return self.title
    

class Rating(Base):
    course = models.ForeignKey(Course, related_name='ratings',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.DecimalField(decimal_places=1, max_digits=2)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'course']
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.name}, {self.course}: {self.rating}'
