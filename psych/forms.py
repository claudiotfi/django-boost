from django import forms
from .utils import get_config

class ConfigForm(forms.Form):
    siteName = forms.CharField(label='Nome do Site', max_length=100)
    siteTheme = forms.ChoiceField(label='Tema do Site', choices=[], widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        site_themes = kwargs.pop('site_themes', [])
        super().__init__(*args, **kwargs)
        self.fields['siteTheme'].choices = [(theme, theme) for theme in site_themes]
