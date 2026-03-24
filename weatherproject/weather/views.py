from django.shortcuts import render

# Create your views here.
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