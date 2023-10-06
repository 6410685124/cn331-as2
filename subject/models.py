from collections.abc import Iterable
from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Class(models.Model):
    YEAR_CHOICES = (
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    )

    SEMESTER_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    name = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_name")
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    students = models.ManyToManyField(Student, related_name='classes')
    max_seats = models.PositiveIntegerField(default=99)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} - {self.semester} - {self.name}"
    
    @property
    def total_seats(self):
        return self.students.count()
    
    @property
    def remaining_seats(self):
        max_seat = self.max_seats
        total_seat = self.total_seats
        return max_seat - total_seat
    