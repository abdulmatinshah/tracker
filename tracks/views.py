from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.views import View
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView)
from .models import Track, Sender
from .forms import UpdateForm

User = get_user_model()

# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class IndexView(TemplateView):
    template_name = 'tracks/index.html'


class TrackView(ListView):
    queryset = Track.objects.incomplete()
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['senders'] = Sender.objects.all()
    #     return context


class TrackDetail(DetailView):
    model = Track


class TrackUpdate(UpdateView):
    model = Track
    form_class = UpdateForm


class OverdueListView(ListView):
    queryset = Track.objects.filter(cutoff_date__lte=timezone.now())


class SenderWiseListView(ListView):

    def get_queryset(self):
        sender = Sender.objects.filter(pk=self.kwargs.get('sender_pk')).first()
        qs = Track.objects.incomplete().filter(sender=sender)
        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     assignees = User.objects.exclude(pk=1)
    #     context['assignees'] = assignees
    #     return context


class AssigneeWiseListView(ListView):

    def get_queryset(self):
        assignee = User.objects.filter(pk=self.kwargs.get('assignee_pk')).first()
        qs = Track.objects.incomplete().filter(assignee=assignee)
        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     assignees = User.objects.exclude(pk=1)
    #     context['assignees'] = assignees
    #     return context
