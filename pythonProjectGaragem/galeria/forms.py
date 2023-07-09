from django import forms
from django.core.exceptions import ValidationError

from galeria.models import GaleriaBD


class Subir(forms.ModelForm):
    class Meta:
        model = GaleriaBD
        fields = "__all__"




