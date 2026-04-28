from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def index(request):
    # Get students who have secured an "O" grade
    students = Student.objects.filter(grade='O').order_by('name')
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        course = request.POST.get('course')
        grade = request.POST.get('grade')
        
        if Student.objects.filter(usn=usn).exists():
            messages.error(request, f"Student with USN {usn} already exists!")
        else:
            Student.objects.create(
                name=name,
                usn=usn,
                course=course,
                grade=grade.upper() # To handle lowercase "o"
            )
            messages.success(request, f"Student {name} added successfully!")
            
    return redirect('index')
