import jsonfield
from django.db import models
from .utils import from_cyrillic_to_eng


def default_urls():
    return {"hh_ru": "", "habr_com": ""}


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование населенного пункта",
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = "Наименование населенного пункта"
        verbose_name_plural = "Наименование  населенных пунктов"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class ComputerLanguage(models.Model):
    name = models.CharField(max_length=50, verbose_name="Язык програмирования",
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = "Язык програмирования"
        verbose_name_plural = "Языки програмирования"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Заголовок вакансии")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание вакансии")
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="Город")
    computer_language = models.ForeignKey("ComputerLanguage", on_delete=models.CASCADE,
                                          verbose_name="Язык программирования")
    timestamp = models.DateField(verbose_name="Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title


class Url(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="Город")
    computer_language = models.ForeignKey("ComputerLanguage", on_delete=models.CASCADE,
                                          verbose_name="Язык программирования")
    url_data = jsonfield.JSONField(default=default_urls)
    
    class Meta:
        unique_together = ("city", "computer_language")


class Errors(models.Model):
    timestamp = models.DateField(verbose_name="Дата добавления", auto_now_add=True)
    data = jsonfield.JSONField()

    class Meta:
        verbose_name = "Ошибка"
        verbose_name_plural = "Ошибки"

    def __str__(self):
        return "Ошибка"


