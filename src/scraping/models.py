from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование населенного пункта")
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Наименование населенного пункта"
        verbose_name_plural = "Наименование населенных пунктов"

    def __str__(self):
        return self.name
