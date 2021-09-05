from django import template
from django.conf import settings
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def plausible(context, site_domain=None, plausible_domain=None, script_name=None):
    request = context["request"]

    if plausible_domain is None:
        plausible_domain = getattr(settings, "PLAUSIBLE_DOMAIN", "plausible.io")
    if script_name is None:
        script_name = getattr(settings, "PLAUSIBLE_SCRIPT_NAME", "plausible.js")
    if site_domain is None:
        site_domain = escape(request.get_host())  # In case of XSS

    attrs = {
        "defer": True,
        "data-domain": site_domain,
        "src": f"https://{plausible_domain}/js/{script_name}",
    }

    # Add a target id for use with compat script
    if "compat" in script_name:
        attrs["id"] = "plausible"

    return mark_safe(f"<script{flatatt(attrs)}></script>")
