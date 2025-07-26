from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class LoginAuthView(LoginView):
    form_class = AuthenticationForm
    template_name = 'Login/login.html'
