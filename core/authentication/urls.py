from django.urls import path

from core.authentication.views import LoginAuthView

urlpatterns = [
    path('', LoginAuthView.as_view(), name='login'),
]
