from datetime import timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from system.forms import PatientForm, LocationForm, VisitForm, SearchForm
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


class UserSearchConnections(TemplateView):
    template_name = 'search_connections.html'

    def get(self, request):
        form = SearchForm
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data['patient']
            window = form.cleaned_data['window']
            form = SearchForm()

        visit_list = patient.visit_set.exclude(
            patient__visit__category__in=["Residential", "Workplace"])

        connection_list = [
            Visit.objects.filter(
                location=visit.location
            ).exclude(
                D_from__gt=visit.D_to + timedelta(days=+window)
            ).exclude(
                D_to__lt=visit.D_from + timedelta(days=-window)
            ).exclude(
                patient=patient
            ).exclude(
                category__in=["Residential", "Workplace"]
            ) for visit in visit_list
        ]
        visit_connection_list = zip(
            visit_list,
            connection_list,
        )

        args = {'form':form, 'patient':patient, 'visit_connection_list':visit_connection_list}
        return render(request, self.template_name, args)

'''
class ConnectionIdentify(TemplateView):
    template_name = 'identify_connection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_pk = self.kwargs['pk']
        window_days = self.request.GET.get('days', None)
        if window_days is None:
            window_days = 0
        else:
            window_days = int(window_days)
        p = Patient.objects.get(pk=patient_pk)
        context['patient'] = p
        context['visit_list'] = p.visit_set.exclude(
            patient__visit__category__in=["Residential", "Workplace"])
        context['connections'] = [
            Visit.objects.filter(
                location=visit.location
            ).filter(
                Q(D_from__lte=visit.D_to + timedelta(days=+window_days)) |
                Q(D_to__gte=visit.D_from + timedelta(days=-window_days)),
            ).exclude(
                patient=context['patient']
            ).exclude(
                category__in=["Residential", "Workplace"]
            ) for
            visit in
            context['visit_list']
        ]
        context['visit_connections_list'] = zip(
            context['visit_list'],
            context['connections'],
        )
        context['window_days'] = window_days
        return context
'''