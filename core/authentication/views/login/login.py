from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginAuthView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['signup_url'] = reverse_lazy('authentication:signup')
        return context
