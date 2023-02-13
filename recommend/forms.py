from django import forms
from .models import GENDER_CHOICES

GENDER_CHOICES = GENDER_CHOICES + [('', '---------')]

class ProfileSearchForm(forms.Form):
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=False)
    yearly_income = forms.IntegerField(label='年収(以上)', required=False)
    height = forms.FloatField(label='身長(以上)', required=False)
    weight = forms.FloatField(label='体重(以下)', required=False)


ProfileSearchFormSet = forms.formset_factory(ProfileSearchForm, extra=3)
