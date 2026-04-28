from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee

def index(request):
    # Get employees whose salary exceeds 50000
    employees = Employee.objects.filter(salary__gt=50000).order_by('-salary')
    return render(request, 'employees/index.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_hiring = request.POST.get('date_of_hiring')
        job_title = request.POST.get('job_title')
        salary = request.POST.get('salary')
        
        if Employee.objects.filter(email=email).exists():
            messages.error(request, f"Employee with email {email} already exists!")
        else:
            Employee.objects.create(
                name=name,
                email=email,
                phone=phone,
                date_of_hiring=date_of_hiring,
                job_title=job_title,
                salary=salary
            )
            messages.success(request, f"Employee {name} added successfully!")
            
    return redirect('index')
