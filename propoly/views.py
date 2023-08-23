from django.shortcuts import render
from .forms import ExampleForm
from django.contrib import messages

cities = [
    "Tokyo",
    "Delhi",
    "Shanghai",
    "São_Paulo",
    "Mexico_City",
    "Cairo",
    "Mumbai",
    "Beijing",
    "Dhaka",
    "Osaka",
    "New_York",
    "Karachi",
    "Buenos_Aires",
    "Chongqing",
    "Istanbul",
    "Kolkata",
    "Manila",
    "Lagos",
    "Rio_de_Janeiro",
    "Tianjin",
    "Kinshasa",
    "Guangzhou",
    "Los_Angeles",
    "Moscow",
    "Shenzhen",
    "Lahore",
    "Bangalore",
    "Paris",
    "Bogotá",
    "Jakarta",
    "Chennai",
    "Lima",
    "Bangkok",
    "Seoul",
    "Nagoya",
    "Hyderabad",
    "London",
    "Tehran",
    "Chicago",
    "Chengdu",
    "Nanjing",
    "Wuhan",
    "Ho_Chi_Minh_City",
    "Luanda",
    "Ahmedabad",
    "Kuala_Lumpur",
    "Xi'an",
    "Hong_Kong",
    "Dongguan",
    "Hangzhou",
    "Foshan",
    "Shenyang",
    "Riyadh",
    "Baghdad",
    "Santiago",
    "Surat",
    "Madrid",
    "Suzhou",
    "Pune",
    "Harbin",
    "Houston",
    "Dallas",
    "Toronto",
    "Dar_es_Salaam",
    "Miami",
    "Belo_Horizonte",
    "Singapore",
    "Philadelphia",
    "Atlanta",
    "Fukuoka",
    "Khartoum",
    "Barcelona",
    "Johannesburg",
    "Saint_Petersburg",
    "Qingdao",
    "Dalian",
    "Washington,_D.C.",
    "Yangon",
    "Alexandria",
    "Jinan",
    "Guadalajara"
]


def index(request):
    return render(request, "index.html")


def profile(request):
    return render(request, template_name="profile.html")


def form_view(request):
    if request.method == "GET":
        form = ExampleForm()
        context = {"form": form}
        return render(request, "form.html", context=context)

    if request.method == "POST":
        form = ExampleForm(request.POST)
        if not form.is_valid():
            return render(request, template_name="form.html", context={"form": form})
        else:
            messages.info(request, "Success")
            response = render(request, "form_success.html")
            response.headers["X-Up-Accept-Layer"] = 'null'
            return response

def autocomplete(request):
    if request.method == "GET":
        if "X-Up-Validate" in request.headers:
            query = request.GET.get("query")
            options = [c for c in cities if query.lower() in c.lower()][:10]
            return render(request, "autocomplete_suggestions.html", context={"options": options})

        return render(request, "autocomplete.html")
