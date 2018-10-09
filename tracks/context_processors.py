from .models import Sender
from django.contrib.auth import get_user_model

User = get_user_model()


def senders(request):
    sender = Sender.objects.all()
    return {'senders': sender}


def assignees(request):
    if request.user and request.user.is_superuser:
        users = User.objects.exclude(pk=1)
        return {'assignees': users}
    return {}
