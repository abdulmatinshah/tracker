from django.conf import settings
from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.


class Sender(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    cell = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class CompletionQuerySet(models.QuerySet):

    def complete(self):
        return self.filter(complete=True)

    def incomplete(self):
        return self.filter(complete=False)


class TrackManager(models.Manager):

    def get_queryset(self):
        return CompletionQuerySet(self.model, using=self._db)

    def complete(self):
        return self.get_queryset().complete()

    def incomplete(self):
        return self.get_queryset().incomplete()


class Track(models.Model):
    # slug = models.SlugField(null=True)
    sender = models.ForeignKey(Sender, on_delete=models.SET_NULL, null=True)
    # r_from = models.CharField(max_length=100, verbose_name='Received From')
    c_name = models.CharField(max_length=100, verbose_name='Complainant Name')
    c_address = models.CharField(max_length=250, verbose_name='Complainant Address')
    gist = models.TextField(null=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    cutoff_date = models.DateField()
    action_required = models.TextField(null=True, blank=True)
    action_taken = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TrackManager()

    class Meta:
        ordering = ['-updated', ]

    def __str__(self):
        return self.c_name

    def get_absolute_url(self):
        return reverse('tracks:detail', kwargs={'pk': self.pk})

    @property
    def is_overdue(self):
        return date.today() > self.cutoff_date
