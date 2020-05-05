from django.views.generic import TemplateView

from system.models import Visit, Patient, Location


# Create your views here.
class UserViewAllPatients(TemplateView):
    template_name = 'patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_list'] = Patient.objects.all()
        return context


class UserViewAllVisits(TemplateView):
    template_name = 'visits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.all()
        return context


class UserViewAllLocations(TemplateView):
    template_name = 'locations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context


class UserViewOnePatient(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        caseID = self.kwargs['caseID']

        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(id=caseID)
        context['patient'] = patient
        context['visit_list'] = patient.visit_set.all()
        return context
