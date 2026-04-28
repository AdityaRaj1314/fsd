# Student Exam Fee Project

This is a Django application to manage student exam fee statuses. It allows you to:
- Add a new student's details (Name, USN, Semester, Exam Fee Status).
- View a list of all students in the database.
- Delete all students who have not paid their exam fees.

---

## 🚀 Setup Instructions (For Cloning to a New PC)

Follow these steps if you are just downloading or cloning this repository to run the project.

### 1. Navigate to the project directory
Open your terminal or command prompt and change the directory to where `manage.py` is located:
```bash
cd examfee_project
```

### 2. Create and activate a Virtual Environment
It's good practice to run Django projects in a virtual environment.
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Install Django and any other required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Create the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
Then, open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ How to Build This From Scratch (Step-by-Step Guide)

If you want to recreate this exact project from scratch yourself, follow these steps in order. It tells you exactly what commands to run, what folders to create, and what code to write.

### Step 1: Create the Project and App
1. Open your terminal and install Django if you haven't already:
   ```bash
   pip install django
   ```
2. Create the main Django project called `examfee_project`:
   ```bash
   django-admin startproject examfee_project
   ```
3. Move into the project directory:
   ```bash
   cd examfee_project
   ```
4. Create an application called `students` inside the project:
   ```bash
   python manage.py startapp students
   ```

### Step 2: Register the App
Open the file `examfee_project/settings.py` and add `'students'` to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students', # <-- Add this line
]
```

### Step 3: Create the Database Model
Open `students/models.py` and define the `Student` model:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField()
    fee_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.usn})"
```

### Step 4: Apply Migrations
Tell Django to create the database table for the `Student` model by running these commands in your terminal:
```bash
python manage.py makemigrations students
python manage.py migrate
```

### Step 5: Create the HTML Template
1. Inside the `students` app directory, create a folder named `templates`.
2. Inside the `templates` folder, create another folder named `students`.
   *(Your folder structure should look like this: `students/templates/students/`)*
3. Inside that final `students` folder, create a file named `index.html` and add the frontend code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Exam Fee Status</title>
</head>
<body>
    <h2>Student Exam Fee Management</h2>
    
    <!-- Form to Add Student -->
    <form method="POST" action="{% url 'add_student' %}">
        {% csrf_token %}
        <label>Name:</label> <input type="text" name="name" required><br>
        <label>USN:</label> <input type="text" name="usn" required><br>
        <label>Semester:</label> <input type="number" name="semester" required><br>
        <label>Fee Paid:</label> <input type="checkbox" name="fee_paid" value="True"><br>
        <button type="submit">Add Student</button>
    </form>

    <!-- Form to Delete Unpaid -->
    <form method="POST" action="{% url 'delete_unpaid' %}">
        {% csrf_token %}
        <button type="submit">Delete Unpaid Students</button>
    </form>

    <!-- List of Students -->
    <table border="1">
        <tr><th>Name</th><th>USN</th><th>Semester</th><th>Fee Status</th></tr>
        {% for student in students %}
        <tr>
            <td>{{ student.name }}</td>
            <td>{{ student.usn }}</td>
            <td>{{ student.semester }}</td>
            <td>{% if student.fee_paid %}Paid{% else %}Not Paid{% endif %}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

### Step 6: Create the Views (Logic)
Open `students/views.py` and add the logic to handle showing, adding, and deleting students:
```python
from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            semester=request.POST.get('semester'),
            fee_paid=request.POST.get('fee_paid') == 'True'
        )
    return redirect('index')

def delete_unpaid(request):
    if request.method == 'POST':
        Student.objects.filter(fee_paid=False).delete()
    return redirect('index')
```

### Step 7: Create App URLs
In the `students` app directory, create a new file called `urls.py` to route traffic to your views:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('delete-unpaid/', views.delete_unpaid, name='delete_unpaid'),
]
```

### Step 8: Connect App URLs to the Main Project
Open the main project's URL file at `examfee_project/urls.py` and tell it to include your `students.urls`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')), # <-- Add this line to connect the app
]
```

### Step 9: Run the Server
Finally, run the server to see your application!
```bash
python manage.py runserver
```
