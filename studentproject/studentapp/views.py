from django.shortcuts import render, redirect
from .models import Student

def student_form(request):
    if request.method=="POST":
        name=request.POST.get("name")
        usn=request.POST.get("usn")
        subject_code=request.POST.get("subject")
        marks=request.POST.get("marks")

        Student.objects.create(
            name=name,
            usn=usn,
            subject_code=subject_code,
            cie_marks=marks
        )
        # Redirect to the results page after submitting the form
        return redirect('/lowcie/')
    
    return render(request, "form.html")
def low_cie_students(request):
    students=Student.objects.filter(cie_marks__lt=20)
    return render(request,"result.html",{"students":students})