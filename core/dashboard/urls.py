from django.urls import path

from core.dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
