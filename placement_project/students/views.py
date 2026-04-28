from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def index(request):
    # Get students placed in Amazon (case-insensitive)
    students = Student.objects.filter(company_name__iexact='Amazon').order_by('name')
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        usn = request.POST.get('usn')
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        
        if Student.objects.filter(usn=usn).exists():
            messages.error(request, f"Student with USN {usn} already exists!")
        else:
            Student.objects.create(
                usn=usn,
                name=name,
                company_name=company_name
            )
            messages.success(request, f"Student {name} added successfully!")
            
    return redirect('index')
