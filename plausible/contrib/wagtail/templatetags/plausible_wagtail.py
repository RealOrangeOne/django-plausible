from django import template

from plausible.contrib.wagtail.models import PlausibleSettings
from plausible.templatetags.plausible import plausible as plausible_tag

register = template.Library()


@register.simple_tag(takes_context=True)
def plausible(context):
    plausible_settings = PlausibleSettings.for_request(context["request"])

    return plausible_tag(
        context,
        plausible_settings.site_domain
        or None,  # `None` so it defaults to request hostname
        plausible_settings.plausible_domain,
        plausible_settings.script_name,
    )
