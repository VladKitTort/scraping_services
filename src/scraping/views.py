from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    city = request.GET.get("city")
    computer_language = request.GET.get("computer_language")
    vacancy = Vacancy.objects.all().order_by("-id")
    if city or computer_language:
        _filter = {}
        if city:
            _filter["city__name"] = city
        if computer_language:
            _filter["computer_language__name"] = computer_language.title()
        vacancy = Vacancy.objects.filter(**_filter).order_by("-id")
    qs = {
        "object_list": vacancy,
    }
    return render(request, "scraping/home.html", qs)
