from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProfilesConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('accounts')

    def ready(self):
        import accounts.signals  # noqa