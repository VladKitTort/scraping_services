from django.contrib import admin
from .models import City, ComputerLanguage, Vacancy, Errors, Url

admin.site.register(City)
admin.site.register(ComputerLanguage)
admin.site.register(Vacancy)
admin.site.register(Errors)
admin.site.register(Url)
