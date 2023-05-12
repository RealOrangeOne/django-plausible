from django.db import models
from wagtail.contrib.settings.models import register_setting

# FIXME: Remove after support for Wagtail 5.0 is dropped
try:
    from wagtail.contrib.settings.models import BaseSiteSetting
except ImportError:
    # Prior to Wagtail 3.0, the only setting available was based on the Site
    from wagtail.contrib.settings.models import BaseSetting as BaseSiteSetting

from .validators import PlausibleScriptNameValidator


@register_setting
class PlausibleSettings(BaseSiteSetting):
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
