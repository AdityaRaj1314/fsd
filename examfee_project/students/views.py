from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def index(request):
    students = Student.objects.all().order_by('semester', 'usn')
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        semester = request.POST.get('semester')
        fee_paid = request.POST.get('fee_paid') == 'True'
        
        # Check if USN already exists
        if Student.objects.filter(usn=usn).exists():
            messages.error(request, f"Student with USN {usn} already exists!")
        else:
            Student.objects.create(
                name=name,
                usn=usn,
                semester=semester,
                fee_paid=fee_paid
            )
            messages.success(request, f"Student {name} added successfully!")
            
    return redirect('index')

def delete_unpaid(request):
    if request.method == 'POST':
        deleted_count, _ = Student.objects.filter(fee_paid=False).delete()
        if deleted_count > 0:
            messages.success(request, f"Successfully deleted {deleted_count} student(s) who haven't paid.")
        else:
            messages.success(request, "No unpaid students found to delete.")
    return redirect('index')
