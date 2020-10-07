import codecs
import os
import sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "django_job_scraping.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, ComputerLanguage

parsers = (
    (hh_ru, "https://ekaterinburg.hh.ru/search/vacancy?search_period=1&clusters=true&area=3&text=Python&"
            "items_on_page=100&order_by=publication_time&search_field=name&no_magic=true&enable_snippets=true"),
    (habr_com, "https://career.habr.com/vacancies?city_id=693&q=Python&sort=date&type=all"),
)
city = City.objects.filter(slug="ekaterinburg").first()
computer_language = ComputerLanguage.objects.filter(slug="python").first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, computer_language=computer_language)
    try:
        v.save()
    except DatabaseError:
        pass

# h = codecs.open("job.json", "w", "utf-8")
# h.write(str(jobs))
# h.close()
#
# h = codecs.open("errors.txt", "w", "utf-8")
# h.write(str(errors))
# h.close()
