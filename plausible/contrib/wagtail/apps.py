from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailPlausibleAppConfig(AppConfig):
    name = "plausible.contrib.wagtail"
    label = "wagtailplausible"

    verbose_name = _("Wagtail Plausible")
