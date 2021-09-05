from django import template
from django.conf import settings
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def plausible(
    context, hostname=None, plausible_domain=None, plausible_script_name=None
):
    request = context["request"]

    if plausible_domain is None:
        plausible_domain = getattr(settings, "PLAUSIBLE_DOMAIN", "plausible.io")
    if plausible_script_name is None:
        plausible_script_name = getattr(
            settings, "PLAUSIBLE_SCRIPT_NAME", "plausible.js"
        )
    if hostname is None:
        hostname = escape(request.get_host())  # In case of XSS

    attrs = {
        "defer": True,
        "data-domain": hostname,
        "src": f"https://{plausible_domain}/js/{plausible_script_name}",
    }

    return mark_safe(f"<script{flatatt(attrs)}></script>")
