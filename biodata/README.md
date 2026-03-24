# Biodata Project - Step-by-Step Guide

This project takes a user's biodata through an HTML form and displays it on a result page. It demonstrates how to handle POST requests without saving to a database.

## 🚀 How to Run the Existing Project

1. Activate your virtual environment: `& "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"`
2. Navigate to this project: `cd "c:\Users\Aditya Raj\fsd\biodata"`
3. Start the server: `python manage.py runserver`
4. Open your browser and go to `http://127.0.0.1:8000/`.

---

## 🛠️ Step-by-Step Instructions: Building it from Scratch

### Step 1: Create the Project and App

```bash
django-admin startproject biodata
cd biodata
python manage.py startapp bioapp
```

### Step 2: Register your Application

📍 **File to Edit:** `biodata/settings.py`
Add `bioapp` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ... other apps
    'bioapp',
]
```

### Step 3: Write the View Logic

The view processes the POST request to capture form data and render it.

📍 **File to Edit:** `bioapp/views.py`

```python
from django.shortcuts import render

def biodata(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        return render(request, "result.html", {
            "name": name,
            "age": age,
            "email": email,
            "phone": phone,
            "address": address,
        })
    return render(request, "form.html")
```

### Step 4: Map the App URLs

📍 **File to Create/Edit:** `bioapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.biodata, name='biodata'),
]
```

### Step 5: Connect App URLs to Project URLs

📍 **File to Edit:** `biodata/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bioapp.urls')),
]
```

### Step 6: Create Templates

Create a new folder named `templates` inside `bioapp`. Then create two files:

📍 **File 1:** `bioapp/templates/form.html`
Create an HTML form with `method="POST"` containing fields for name, age, email, phone, and address. Include `{% csrf_token %}` inside the form.

📍 **File 2:** `bioapp/templates/result.html`
Display the data passed from the view using Django template tags: `{{ name }}`, `{{ age }}`, etc.

### Step 7: Run the Server

```bash
python manage.py runserver
```
