from django import forms
from .models import Importer
from multiselectfield import MultiSelectField


class ImporterForm(forms.ModelForm):
    class Meta:
        model = Importer
        fields = '__all__'