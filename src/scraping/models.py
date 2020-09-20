from django.db import models
from .utils import from_cyrillic_to_eng


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