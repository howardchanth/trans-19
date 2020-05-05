from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib import messages

from system.forms import PatientForm, LocationForm, VisitForm
from system.models import Visit, Patient, Location


# Create your views here.
class UserViewAllPatients(TemplateView):
    template_name = 'view_patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_list'] = Patient.objects.all()
        return context


class UserViewAllVisits(TemplateView):
    template_name = 'view_visits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.all()
        return context


class UserViewAllLocations(TemplateView):
    template_name = 'view_locations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context


class UserViewOnePatient(TemplateView):
    template_name = 'view_details.html'

    def get_context_data(self, **kwargs):
        patient_pk = self.kwargs['pk']

        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(pk=patient_pk)
        context['patient'] = patient
        context['visit_list'] = patient.visit_set.all()
        return context


class UserCreateOnePatient(CreateView):
    template_name = 'create_patient.html'
    form_class = PatientForm
    success_url = "/system/create_patient"

    def form_valid(self, form):
        self.object = form.save()

        return HttpResponseRedirect("/system/create_patient")


class UserCreateOneLocation(CreateView):
    template_name = 'create_location.html'
    form_class = LocationForm
    success_url = "/system/create_location"

    def form_valid(self, form):
        self.object = form.save()

        return HttpResponseRedirect("/system/create_location")


class UserCreateOneVisit(CreateView):
    template_name = 'create_visit.html'
    form_class = VisitForm
    success_url = "/system/create_visit"

    def form_valid(self, form):
        self.object = form.save()

        return HttpResponseRedirect("/system/create_visit")


class UserUpdateOnePatient(UpdateView):
    template_name = 'update_patient.html'
    model = Patient
    form_class = PatientForm
    success_url = "/system/view_patients"


class UserUpdateOneLocation(UpdateView):
    template_name = 'update_location.html'
    model = Location
    form_class = LocationForm
    success_url = "/system/view_locations"


class UserUpdateOneVisit(UpdateView):
    template_name = 'update_visit.html'
    model = Visit
    form_class = VisitForm
    success_url = "/system/view_visits"


class UserDeleteOnePatient(DeleteView):
    template_name = 'delete_patient.html'
    model = Patient
    success_url = "/system/view_patients"


class UserDeleteOneLocation(DeleteView):
    template_name = 'delete_location.html'
    model = Location
    success_url = "/system/view_locations"


class UserDeleteOneVisit(DeleteView):
    template_name = 'delete_visit.html'
    model = Visit
    success_url = "/system/view_visits"