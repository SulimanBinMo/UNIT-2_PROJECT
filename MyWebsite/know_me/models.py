from django.db import models

# Create your models here.

class Course(models.Model):
    presented_by = models.CharField(max_length=2084)
    title = models.CharField(max_length=2084)
    about_course = models.TextField()
    image = models.ImageField(upload_to="images/")
    course_hours = models.IntegerField()
    start_from = models.DateField()
    end_at = models.DateField()
