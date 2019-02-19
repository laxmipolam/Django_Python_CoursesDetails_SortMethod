from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ChangeDataForm(forms.Form):
    form_summary = forms.CharField(max_length=200, help_text="Enter technologies", required = False)
    form_next_registration = forms.DateField(help_text="Enter registration date. Past date also can be selected")

class SortForm(forms.Form):
    numbers = forms.CharField(widget=forms.Textarea)
    CHOICES=[('Ascending','Ascending'),('Descending','Descending')]

    like = forms.ChoiceField(choices=CHOICES)
    