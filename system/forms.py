import datetime

from django import forms
from django.forms import ModelForm

from system.models import Patient, Location, Visit


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'caseID': 'Case ID',
            'name': 'Patient Name',
            'IDnum': 'ID No.',
            'DoB': 'Date of Birth',
            'DCC': 'Date confirmed',
        }
        cur_year = datetime.datetime.today().year
        year_range = tuple([i for i in range(cur_year - 100, cur_year + 1)])
        widgets = {
            'DoB': forms.SelectDateWidget(years=year_range),
            'DCC': forms.SelectDateWidget(years=year_range),
        }


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'address': 'Address',
            'name': 'Location Name',
            'district': 'District',
            'x': 'X coordinate',
            'y': 'Y coordinate',
        }


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        labels = {
            'patient': 'Patient',
            'location': 'Location',
            'D_from': 'Date from',
            'D_to': 'Date to',
            'detail': 'Visit details',
            'category': 'Category',
        }
        cur_year = datetime.datetime.today().year
        year_range = tuple([i for i in range(cur_year - 100, cur_year + 1)])
        widgets = {
            'D_from': forms.SelectDateWidget(years=year_range),
            'D_to': forms.SelectDateWidget(years=year_range),
        }


class SearchForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    window = forms.IntegerField(min_value=0)
