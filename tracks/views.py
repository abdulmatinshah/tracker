from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.views import View
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView)
from .models import Track
from .forms import UpdateForm
# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class IndexView(TemplateView):
    template_name = 'tracks/index.html'


class TrackView(ListView):
    model = Track


class TrackDetail(DetailView):
    model = Track


class TrackUpdate(UpdateView):
    model = Track
    # fields = ['remarks']
    form_class = UpdateForm
