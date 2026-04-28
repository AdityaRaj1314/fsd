from django.shortcuts import render, redirect
from .models import Student

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        department = request.POST.get('department')
        grade = request.POST.get('grade')
        
        Student.objects.create(
            name=name,
            usn=usn,
            department=department,
            grade=grade
        )
        return redirect('index')
    
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

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
            # Update the first one or handle appropriately, but for simplicity
            student = Student.objects.filter(name=name).first()
            student.grade = new_grade
            student.save()
            updated_student = student
            
    return render(request, 'students/update_grade.html', {'updated_student': updated_student})
