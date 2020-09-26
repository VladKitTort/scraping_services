from django import forms

from scraping.models import City, ComputerLanguage


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name="slug", required=False,
                                  widget=forms.Select(attrs={"class": "form-control"}),
                                  label="Город")
    computer_language = forms.ModelChoiceField(queryset=ComputerLanguage.objects.all(),
                                               to_field_name="slug", required=False,
                                               widget=forms.Select(attrs={"class": "form-control  ml-4"}),
                                               label="Язык программирования")

