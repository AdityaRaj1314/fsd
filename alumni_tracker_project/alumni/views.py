from django.shortcuts import render, redirect
from .models import Alumni

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        passing_year = request.POST.get('passing_year')
        company = request.POST.get('company')
        
        Alumni.objects.create(
            name=name,
            usn=usn,
            passing_year=passing_year,
            company=company
        )
        return redirect('index')
        
    return render(request, 'alumni/index.html')

def search(request):
    year = request.GET.get('year')
    alumni_list = None
    
    if year:
        alumni_list = Alumni.objects.filter(passing_year=year)
        
    return render(request, 'alumni/search.html', {'alumni_list': alumni_list, 'year': year})
