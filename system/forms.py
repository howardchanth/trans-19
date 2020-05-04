from django import forms
from system.models import Patient, Location


class PatientForm(forms.Form):
    caseID = forms.IntegerField()
    name = forms.CharField()
    IDnum = forms.CharField()
    DoB = forms.DateField()
    DCC = forms.DateField()



class LocationForm(forms.Form):

    name = forms.CharField()
    address = forms.CharField()
    district = forms.CharField()
    x = forms.IntegerField()
    y = forms.IntegerField()



class Visit(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    location = forms.ModelChoiceField(queryset=Location.objects.all())

    D_from = forms.DateField()
    D_to = forms.DateField()

    detail = forms.CharField()
    category = forms.CharField()
