from django.shortcuts import render, redirect
from .models import Alumni

def index(request):
    year = request.GET.get('year')
    alumni_list = None
    if year:
        alumni_list = Alumni.objects.filter(passing_year=year)
        
    return render(request, 'alumni/index.html', {
        'alumni_list': alumni_list,
        'year': year
    })

def add_alumni(request):
    if request.method == 'POST':
        usn = request.POST.get('usn')
        if not Alumni.objects.filter(usn=usn).exists():
            Alumni.objects.create(
                name=request.POST.get('name'),
                usn=usn,
                passing_year=request.POST.get('passing_year'),
                company=request.POST.get('company')
            )
    return redirect('index')
