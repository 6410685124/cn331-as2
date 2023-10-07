from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import F

from subject.models import Student, Subject, Class
from .forms import QuotaRequestForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    student = Student.objects.get(student_id=request.user.username)
    registered_courses = student.classes.filter(status=True)
    available_courses = Class.objects.exclude(id__in=registered_courses.values_list('id', flat=True)).filter(status=True)
    return render(request, 'student/index.html', {
        'registred_class': registered_courses,
        'available_class': available_courses,
        'student': student
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'student/login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, "student/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'student/login.html', {
        'message': 'Logged out'
    })

def add_student_to_class(request, student_id, name):
    my_class = get_object_or_404(Class, name=name)
    student = get_object_or_404(Student, student_id=student_id)
    my_class.add_student(student)
    return redirect('index')

def remove_student_from_class(request, student_id, name):
    my_class = get_object_or_404(Class, name=name)
    student = get_object_or_404(Student, student_id=student_id)
    my_class.remove_student(student)
    return redirect('index')

def class_detail(request, name):
    # my_class = Class.objects.get(name=name)
    my_class = get_object_or_404(Class, name=name)
    return render(request, 'student/class_detail.html', {'class_obj' : my_class})