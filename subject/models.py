from collections.abc import Iterable
from django.db import models

# Create your models here.

class Subject(models.Model):

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.code

class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, unique=True)
    YEAR_CHOICES = (
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    )

    year = models.CharField(max_length=10, default=None, choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.last_name}"


class Class(models.Model):

    name = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_name", to_field='code')
    students = models.ManyToManyField(Student, related_name='classes')
    max_seats = models.PositiveIntegerField(default=99)
    
    SEMESTER_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    semester = models.CharField(max_length=10, default=None, choices=SEMESTER_CHOICES)

    def __str__(self):
        return f"{self.name}"
    
    status = models.BooleanField(default=True)
    @property
    def total_seats(self):
        return self.students.count()
    
    @property
    def remaining_seats(self):
        max_seat = self.max_seats
        total_seat = self.total_seats
        return max_seat - total_seat
    
    def add_student(self, student):
        self.students.add(student)

    def remove_student(self, student):
        self.students.remove(student)
    