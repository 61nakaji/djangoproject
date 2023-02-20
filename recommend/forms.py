from django import forms
from .models import MODE_CHOICES

from django.contrib.auth.forms import AuthenticationForm


MODE_CHOICES = MODE_CHOICES + [('', '---------')]


class ProfileSearchForm(forms.Form):
    name = forms.CharField(label='曲名', required=False)
    album = forms.CharField(label='アルバム名', required=False)
    artist = forms.CharField(label='アーティスト名', required=False)
    length = forms.IntegerField(label='曲の長さ(以下)', required=False)
    gender = forms.ChoiceField(
        label='曲調', choices=MODE_CHOICES, required=False)
    popularity = forms.IntegerField(label='人気度(以上)', required=False)
    danceability = forms.FloatField(label='ダンス度(以上)', required=False)
    acousticness = forms.FloatField(label='アコースティック度(以上)', required=False)


ProfileSearchFormSet = forms.formset_factory(ProfileSearchForm, extra=3)


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
