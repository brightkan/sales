from django import forms

from salesapp.models import CSV


class CSVModelForm(forms.ModelForm):
    class Meta:
        model = CSV
        fields = ('file_name',)

