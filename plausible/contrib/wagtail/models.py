from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting

from .validators import PlausibleScriptNameValidator


@register_setting
class PlausibleSettings(BaseSetting):
    site_domain = models.CharField(max_length=255, null=False, blank=True)
    plausible_domain = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        default="plausible.io",
    )
    script_name = models.CharField(
        max_length=255,
        validators=[PlausibleScriptNameValidator()],
        default="plausible.js",
    )

    class Meta:
        verbose_name = "Plausible Analytics"
