from django.shortcuts import render

# Create your views here.
def home(request):
    name=None
    if request.method=="POST":
        name=request.POST.get("username")
    return render(request, 'index.html', {'name': name})