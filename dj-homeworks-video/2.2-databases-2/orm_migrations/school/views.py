from django.shortcuts import render
from django.views.generic import ListView
from .models import Student

def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    students = Student.objects.all().order_by(ordering)
    context = {
        'object_list': students
    }
    return render(request, template, context)
