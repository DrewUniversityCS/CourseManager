from allauth.account.forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from database.forms import PreferencesFormForm
from database.models.structural_models import PreferenceForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'open_new_prefernce_form': PreferencesFormForm(),
            'all_preference_forms': PreferenceForm.objects.all()
        })
        return context_data


class DocsView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/docs.html'


class StudentFormSuccessView(TemplateView):
    template_name = 'pages/student-form-success.html'


class GenerateScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/generate_schedule.html'


class CheckScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/check_schedule.html'


class CrudView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/crud.html'


class InviteView(LoginRequiredMixin, FormView):
    form_class = SignupForm
    template_name = "account/new_admin_registration_form.html"
    success_url = reverse_lazy('pages:invite-success')

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)
