from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .forms import LoginForm, PrettyLoginForm


class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'


class CustomLoginView(LoginView):
    authentication_form = PrettyLoginForm
    redirect_authenticated_user = True
    # success_url = reverse('accounts:dashboard')


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    context = dict()
    form_class = LoginForm

    def get_success_url(self):
        return reverse('accounts:login')

    def post(self, request):
        form = self.get_form(LoginForm)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            user = authenticate(**form.cleaned_data)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'success {user}'.format(user=user.username))
        return redirect('accounts:login')


