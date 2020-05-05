from django.views.generic import TemplateView, FormView, CreateView

from system.models import Visit, Patient, Location
from system.forms import PatientForm


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

# TODO: Still finding a way to connect this to data
# class UserCreateOnePatient(FormView):
#     template_name = 'create_patient.html'
#     form_class = PatientForm
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)


# TODO: Need to customize field labels by changing the verbose_name of the model field
class UserCreateOnePatient(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'create_patient.html'


class UserCreateOneLocation(CreateView):
    model = Location
    fields = '__all__'
    template_name = 'create_location.html'


class UserCreateOneVisit(CreateView):
    model = Visit
    fields = '__all__'
    template_name = 'create_visit.html'
