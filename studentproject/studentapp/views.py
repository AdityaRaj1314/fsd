from django.shortcuts import render, redirect
from .models import Student

def student_form(request):

    if request.method == "POST":

        usn = request.POST.get("usn")
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        marks = request.POST.get("marks")
        
        # Give marks a default value of 0 if omitted to avoid ValueError
        if not marks:
            marks = 0

        Student.objects.create(
            usn=usn,
            name=name,
            subject_code=subject,
            cie_marks=marks
        )
        
        return redirect('/lowcie/')

    return render(request, "form.html")


def low_cie_students(request):

    students = Student.objects.filter(cie_marks__lt=20)

    return render(request, "result.html", {"students": students})