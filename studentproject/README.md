# Student CIE Marks Tracker

This Django project collects student details (USN, Name, Subject Code, and CIE marks) and displays a filtered list of students who have scored less than 20 in their continuous internal evaluation (CIE).

## How to Execute and Run the Existing Project

1. **Open your terminal or command prompt.**
2. **Activate your Python environment** (if applicable):
   ```powershell
   & "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"
   ```
3. **Navigate into the project directory**:
   ```bash
   cd "c:\Users\Aditya Raj\fsd\studentproject"
   ```
4. **Make and run database migrations** (to ensure the database is ready):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
6. **Open your web browser** and go to `http://127.0.0.1:8000/`.

---

## Complete Project Implementation Guide (Where to Add Code)

If you are continuing the project or building it from scratch, here is exactly what goes in which file:

### 1. Register the Application

**File: `studentproject/settings.py`**
Scroll to `INSTALLED_APPS` and add your app `studentapp`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studentapp', # <-- Add this line
]
```

### 2. Define the Database Tables (Models)

**File: `studentapp/models.py`**
Add the schema for representing a student:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    cie_marks = models.IntegerField()

    def __str__(self):
        return self.name
```

_(After modifying models, always run `python manage.py makemigrations` and `python manage.py migrate`)_

### 3. Create the Business Logic (Views)

**File: `studentapp/views.py`**
Create the functions that handle user requests:

```python
from django.shortcuts import render, redirect
from .models import Student

def student_form(request):
    if request.method == "POST":
        usn = request.POST.get("usn")
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        marks = request.POST.get("marks")

        # Save to database
        if not marks:
            marks = 0

        Student.objects.create(usn=usn, name=name, subject_code=subject, cie_marks=marks)
        return redirect('/lowcie/')

    # GET request - show form
    return render(request, "form.html")

def low_cie_students(request):
    # Fetch students with marks less than 20
    students = Student.objects.filter(cie_marks__lt=20)
    return render(request, "result.html", {"students": students})
```

### 4. Create App-level Routes (URLs)

**File: `studentapp/urls.py`** (You may need to create this file)
Map the views to URLs:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form),
    path('lowcie/', views.low_cie_students),
]
```

### 5. Connect App Routes to Global Project URLs

**File: `studentproject/urls.py`**
Include the `studentapp.urls` into the main application:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentapp.urls')), # <-- Include your app routes
]
```

### 6. Create the User Interface (Templates)

**Folder: `studentapp/templates/`** (You must create the `templates` folder)

**File: `studentapp/templates/form.html`**

```html
<form method="POST">
  {% csrf_token %}
  <!-- Required for security -->
  <input type="text" name="name" placeholder="Name" /><br />
  <input type="text" name="usn" placeholder="USN" /><br />
  <input type="text" name="subject" placeholder="Subject Code" /><br />
  <input type="number" name="marks" placeholder="CIE Marks" /><br />
  <button type="submit">Submit</button>
</form>
```

**File: `studentapp/templates/result.html`**

```html
<h2>Students with Low CIE Marks (< 20)</h2>
<table border="1">
  <tr>
    <th>Name</th>
    <th>USN</th>
    <th>Subject Code</th>
    <th>Marks</th>
  </tr>
  {% for student in students %}
  <tr>
    <td>{{ student.name }}</td>
    <td>{{ student.usn }}</td>
    <td>{{ student.subject_code }}</td>
    <td>{{ student.cie_marks }}</td>
  </tr>
  {% endfor %}
</table>
<a href="/">Go Back</a>
```
