from django.urls import path, include
from .views import (LoginView, DashboardView, CustomLoginView)
app_name = 'accounts'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
