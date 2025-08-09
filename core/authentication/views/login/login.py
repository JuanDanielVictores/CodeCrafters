from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from core.authentication.forms import LoginForm


class LoginAuthView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'
    redirect_authenticated_user = True


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['signup_url'] = reverse_lazy('authentication:signup')
        return context
