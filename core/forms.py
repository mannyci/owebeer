from django import forms
from django.forms.widgets import TextInput, Select, SelectMultiple
from django.forms import ValidationError
from django.utils.safestring import mark_safe
from .models import Team
from account.models import Account

class NewTeamForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Team name', 'autofocus': 'true'}))
    description = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))

    class Meta:
        model = Team
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Team.objects.filter(name=name, name__iexact=name).exists():
            team = Team.objects.get(name=name)
            raise ValidationError(
                mark_safe(('Team {0} with that name already exists, click <a href="{0}">here</a>').format(host))
            )
        return name


class TeamUpdateForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    members = forms.ModelMultipleChoiceField(required=False, queryset=Account.objects.all(), widget=SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Team
        fields = ['name', 'description', 'members']
