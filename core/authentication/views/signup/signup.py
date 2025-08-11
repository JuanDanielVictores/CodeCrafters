from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from core.authentication.forms import SignupForm


class SignupView(FormView):
    template_name = 'signup/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('authentication:login')

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro - Code Crafters'
        context['back_url'] = self.success_url
        return context

