from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages


# Create your views here.
def index(request):
    company = request.GET.get('company', '')
    if company:
        students = Student.objects.filter(company_name__iexact=company).order_by('name')
    else:
        students = Student.objects.all().order_by('name')
    return render(request, "students/index.html", {'students': students, 'company': company})

def add_student(request):
    if request.method=="POST":
        name=request.POST.get('name')
        usn=request.POST.get('usn')
        company_name=request.POST.get('company_name')
        if Student.objects.filter(usn=usn).exists():
            messages.error(request,f"student {usn}already exist")
        else:
            Student.objects.create(
                name=name,
                usn=usn,
                company_name=company_name
            )
            messages.success(request,f"studnet {name} successfully added")
    return redirect('index')