from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (TemplateView, ListView,)
# from django.views.generic.edit import FormMixin

from .forms import LoginForm, PrettyLoginForm
from tracks.models import Track, Sender


class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'
    # mothing


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


class UserDashboardView(LoginRequiredMixin, ListView):
    paginate_by = 20

    def get_queryset(self):
        qs = Track.objects.filter(assignee=self.request.user)
        return qs


class OverdueListView(LoginRequiredMixin, ListView):
    paginate_by = 20

    def get_queryset(self):
        qs = Track.objects.incomplete().filter(assignee=self.request.user, cutoff_date__lte=timezone.now())
        return qs


class SenderWiseListView(LoginRequiredMixin, ListView):
    paginate_by = 20

    def get_queryset(self):
        sender = Sender.objects.filter(pk=self.kwargs.get('sender_pk')).first()
        qs = Track.objects.incomplete().filter(assignee=self.request.user, sender=sender)
        return qs

