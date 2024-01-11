# election/forms.py

from django import forms

from election_results.models import PollingUnit, LGA


class PollingUnitResultForm(forms.Form):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all())


class LgaResultForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=LGA.objects.all())


class NewPollingUnitResultForm(forms.Form):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all())
    party = forms.CharField(max_length=255)
    result = forms.IntegerField()
