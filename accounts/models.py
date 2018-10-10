from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    abbreviated_name = models.CharField(max_length=20, null=True, blank=True)
    office_phone = models.CharField(max_length=10, null=True, blank=True)
    office_fax = models.CharField(max_length=10, null=True, blank=True)
    cell = models.CharField(max_length=10, null=True, blank=True)
    postal_address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.abbreviated_name




