from django.urls import path

from core.authentication.views.login import LoginAuthView

urlpatterns = [
    path('', LoginAuthView.as_view(), name='login'),
]
