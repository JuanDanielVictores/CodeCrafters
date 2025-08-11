from django.urls import path

from core.authentication.views import LoginAuthView, SignupView

app_name = 'authentication'
urlpatterns = [
    path('', LoginAuthView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
