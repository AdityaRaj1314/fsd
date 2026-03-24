# Feedback Project - Step-by-Step Guide

This project allows users to submit feedback which is stored in a database and rendered dynamically using JsonResponse and models.

## 🚀 How to Run the Existing Project

1. Activate your virtual environment: `& "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"`
2. Navigate to this project: `cd "c:\Users\Aditya Raj\fsd\feedbackproject"`
3. Start the server: `python manage.py runserver`
4. Open your browser and go to `http://127.0.0.1:8000/`.

---

## 🛠️ Step-by-Step Instructions: Building it from Scratch

### Step 1: Create the Project and App

```bash
django-admin startproject feedbackproject
cd feedbackproject
python manage.py startapp feedbackapp
```

### Step 2: Register your Application

📍 **File to Edit:** `feedbackproject/settings.py`  
Add `feedbackapp` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # ... other apps
    'feedbackapp',
]
```

### Step 3: Define the Database Table (Model)

📍 **File to Edit:** `feedbackapp/models.py`

```python
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
```

After defining the model, run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Write the View Logic

The view handles showing all feedback to the user on the home page and adding new feedback via a POST request.

📍 **File to Edit:** `feedbackapp/views.py`

```python
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
```

### Step 5: Map App and Project URLs

📍 **File to Create/Edit:** `feedbackapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_feedback, name='add_feedback'),
]
```

📍 **File to Edit:** `feedbackproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedbackapp.urls')),
]
```

### Step 6: Create Templates

Create a new folder named `templates` inside `feedbackapp`. Then create an `index.html` file.

📍 **File:** `feedbackapp/templates/index.html`
Create a document to loop over existing feedback (`{% for fb in feedbacks %}`) and add a form with `method="POST"` that posts to the `/add/` URL using JavaScript/AJAX or a direct form submission. (Don't forget the `{% csrf_token %}`!).

### Step 7: Run the Server

```bash
python manage.py runserver
```
