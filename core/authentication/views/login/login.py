from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginAuthView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.visible_fields():
            field.field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': f'Ingrese su {field.label.lower()}'
            })
        return form

    def form_invalid(self, form):
        for field in form.visible_fields():
            field.field.widget.attrs.update({
                'class': 'form-control is-invalid',
                'autocomplete': 'off',
                'placeholder': f'Ingrese su {field.label.lower()}'
            })
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['signup_url'] = reverse_lazy('authentication:signup')
        return context
