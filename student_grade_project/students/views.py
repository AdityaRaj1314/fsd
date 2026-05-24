from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            department=request.POST.get('department'),
            grade=request.POST.get('grade')
        )
    return redirect('index')

def update_grade(request):
    updated_student = None
    if request.method == 'POST':
        name = request.POST.get('name')
        new_grade = request.POST.get('grade')
        
        try:
            student = Student.objects.get(name=name)
            student.grade = new_grade
            student.save()
            updated_student = student
        except Student.DoesNotExist:
            updated_student = 'Not Found'
        except Student.MultipleObjectsReturned:
            student = Student.objects.filter(name=name).first()
            student.grade = new_grade
            student.save()
            updated_student = student
            
    return render(request, 'students/update_grade.html', {'updated_student': updated_student})
