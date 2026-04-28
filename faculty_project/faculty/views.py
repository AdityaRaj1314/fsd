from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FacultyMember

def index(request):
    # Get faculty who belong to CSE and have the title Professor
    faculty = FacultyMember.objects.filter(branch__iexact='CSE', title__iexact='Professor').order_by('name')
    return render(request, 'faculty/index.html', {'faculty': faculty})

def add_faculty(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        title = request.POST.get('title')
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        
        if FacultyMember.objects.filter(emp_id=emp_id).exists():
            messages.error(request, f"Faculty with ID {emp_id} already exists!")
        else:
            FacultyMember.objects.create(
                emp_id=emp_id,
                title=title,
                name=name,
                branch=branch
            )
            messages.success(request, f"Faculty {name} added successfully!")
            
    return redirect('index')
