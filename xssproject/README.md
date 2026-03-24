# XSS Project - Step-by-Step Guide

This project demonstrates how data input dynamically alters a webpage. It takes a username and renders it on a single page, which is a foundational concept when discussing cross-site scripting (XSS) and input sanitization.

## 🚀 How to Run the Existing Project

1. Activate your virtual environment: `& "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"`
2. Navigate to this project: `cd "c:\Users\Aditya Raj\fsd\xssproject"`
3. Start the server: `python manage.py runserver`
4. Open your browser and go to `http://127.0.0.1:8000/`.

---

## 🛠️ Step-by-Step Instructions: Building it from Scratch

### Step 1: Create the Project and App

```bash
django-admin startproject xssproject
cd xssproject
python manage.py startapp app2
```

### Step 2: Register your Application

📍 **File to Edit:** `xssproject/settings.py`  
Add `app2` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # ... other apps
    'app2',
]
```

### Step 3: Write the View Logic

The view captures the username string from a POST request and injects it back into the template context.

📍 **File to Edit:** `app2/views.py`

```python
from django.shortcuts import render

def home(request):
    name = None
    if request.method == "POST":
        name = request.POST.get("username")

    return render(request, 'index.html', {'name': name})
```

### Step 4: Map App URLs and Connect to Project

📍 **File to Create/Edit:** `app2/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

📍 **File to Edit:** `xssproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app2.urls')),
]
```

### Step 5: Create Templates

Create a new folder named `templates` inside `app2`. Then create an `index.html` file.

📍 **File:** `app2/templates/index.html`
Create a form that submits a `username` using `POST`. Display the `{{ name }}` variable directly below the form if the `name` is present. _Note: Django automatically escapes strings to prevent real XSS unless explicit safe tags are used._

### Step 6: Run the Server

```bash
python manage.py runserver
```
