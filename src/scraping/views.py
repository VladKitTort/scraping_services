from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm


def home_view(request):
    form = FindForm
    city = request.GET.get("city")
    computer_language = request.GET.get("computer_language")
    vacancy = Vacancy.objects.all().order_by("-id")
    if city or computer_language:
        _filter = {}
        if city:
            _filter["city__slug"] = city
        if computer_language:
            _filter["computer_language__slug"] = computer_language
        vacancy = Vacancy.objects.filter(**_filter).order_by("-id")
    qs = {
        "object_list": vacancy,
        "form": form,
    }
    return render(request, "scraping/home.html", qs)
