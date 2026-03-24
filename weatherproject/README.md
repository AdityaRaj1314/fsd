# Weather Project - Step-by-Step Guide

This project fetches live weather data from OpenWeatherMap API and displays it based on the city requested by the user.
_Prerequisites: `requests` library is required (`pip install requests`)._

## 🚀 How to Run the Existing Project

1. Activate your virtual environment: `& "c:\Users\Aditya Raj\fsd\.venv\Scripts\Activate.ps1"`
2. Navigate to this project: `cd "c:\Users\Aditya Raj\fsd\weatherproject"`
3. Install dependencies: `pip install requests` (if not installed)
4. Start the server: `python manage.py runserver`
5. Open your browser and go to `http://127.0.0.1:8000/`.

---

## 🛠️ Step-by-Step Instructions: Building it from Scratch

### Step 1: Create the Project and App

```bash
django-admin startproject weatherproject
cd weatherproject
python manage.py startapp weather
pip install requests
```

### Step 2: Register your Application

📍 **File to Edit:** `weatherproject/settings.py`  
Add `weather` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # ... other apps
    'weather',
]
```

### Step 3: Write the View Logic (API Call)

The view accepts a POST request with the city name, sends a request to the OpenWeatherMap API, and returns the response.

📍 **File to Edit:** `weather/views.py`

```python
import requests
from django.shortcuts import render

API_KEY = "001358509a4441871a95194d28f754c0"

def home(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather_data = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"].title()
            }
        else:
            error = "Invalid city name. Please try again."

    return render(request, "index.html", {
        "weather": weather_data,
        "error": error
    })
```

### Step 4: Map App and Project URLs

📍 **File to Create/Edit:** `weather/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

📍 **File to Edit:** `weatherproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
]
```

### Step 5: Create Templates

Create a new folder named `templates` inside `weather`. Then create an `index.html` file.

📍 **File:** `weather/templates/index.html`
Create a form with an input for "city" and display the `weather.temp`, `weather.desc`, and `weather.city` variables if `weather` exists, and display the `error` message if the city is invalid.

### Step 6: Run the Server

```bash
python manage.py runserver
```
