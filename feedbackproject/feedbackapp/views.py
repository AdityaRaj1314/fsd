from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback

def home(request):
    feedbacks = Feedback.objects.all()
    return render(request, "index.html", {"feedbacks": feedbacks})


def add_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        feedback = Feedback.objects.create(name=name, message=message)

        return JsonResponse({
            "name": feedback.name,
            "message": feedback.message
        })