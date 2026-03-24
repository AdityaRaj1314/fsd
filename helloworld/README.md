# Django Hello World Project - Step-by-Step Guide

This guide explains how to build and expand this Django Hello World application from scratch. It includes exact instructions on what code goes into which files.

## 🚀 How to Run the Existing Project

1. Open your terminal in VS Code.
2. Activate your virtual environment:
   ```powershell
   & "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"
   ```
3. Navigate into the specific project directory:
   ```bash
   cd "c:\Users\Aditya Raj\fsd\helloworld"
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Click on or navigate to the link provided (usually `http://127.0.0.1:8000/`).

---

## 🛠️ Step-by-Step Instructions: Building it from Scratch

If you want to understand how this was built or practice doing it yourself, follow these steps in your project.

### Step 1: Create the Project and App

_(Assuming you already installed Django via `pip install django`)_

1. Create a new Django project:
   ```bash
   django-admin startproject helloworld
   ```
2. Navigate into the folder:
   ```bash
   cd helloworld
   ```
3. Create an application inside the project:
   ```bash
   python manage.py startapp myapp
   ```

### Step 2: Register your Application

Django needs to know `myapp` exists.

📍 **File to Edit:** `helloworld/settings.py`

Scroll down to the `INSTALLED_APPS` list and add your new app at the bottom:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # <-- Add this line
]
```

### Step 3: Write the View (The Logic)

A view determines what happens when someone visits a specific URL. Let's send a basic HTTP Response.

📍 **File to Edit:** `myapp/views.py`

Replace the content with the following code:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World! This is my first Django app.</h1>")
```

### Step 4: Map the App URL

Now that you have a view, you need a URL path that points to it. First, we create `urls.py` inside the app.

📍 **File to Create/Edit:** `myapp/urls.py`
_(If this file doesn't exist inside `myapp`, create it!)_

Add this code:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # The empty string '' means the root URL
]
```

### Step 5: Connect App URLs to Project URLs

Finally, connect your `myapp` URLs to the main `helloworld` project URLs.

📍 **File to Edit:** `helloworld/urls.py`

Update the file to include the `include` function, and add the path pointing to `myapp.urls`:

```python
from django.contrib import admin
from django.urls import path, include  # <-- Don't forget to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),   # <-- Add this line to include your app's URLs
]
```

### Step 6: Start the Server!

Run this command in the terminal:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser. You should see "Hello World!" on the screen.
