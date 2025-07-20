
from django.urls import path

from core.authentication.views.home import home

urlpatterns = [
    path("", home, name="home"),
]