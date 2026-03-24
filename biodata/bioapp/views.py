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