from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import date


class Major(models.Model):
    name = models.CharField(max_length=200, help_text='Major (e.g. Computer Science)')
    
    def __str__(self):
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Course(models.Model):
    title = models.CharField(max_length=200)

    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief summary of course')
    major = models.ManyToManyField(Major, help_text='Select a major of this course')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns url to access course detail."""
        return reverse('course-detail', args=[str(self.id)])

    def showmajor(self):
        return ', '.join(major.name for major in self.major.all()[:3])
    
    showmajor.short_description = 'Major'

import uuid # Required for unique book instances

class CourseInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Course lecture number')
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True) 
    regstudent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    REG_STATUS = (
        ('c', 'Closed'),
        ('a', 'Available'),
        ('w', 'WaitList')
    )
    next_registration = models.DateField(null=True, blank=True)
    summary = models.CharField(null=True, max_length=200)
    status = models.CharField(
        max_length=1,
        choices=REG_STATUS,
        blank=True,
        default='w',
        help_text='Course availability',
    )

    def __str__(self):
        return f'{self.id} ({self.course.title})'

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'