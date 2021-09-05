from django.template import RequestContext, Template
from pytest_django.asserts import assertInHTML


def _render_string(template, context=None) -> str:
    return Template(template).render(context)


def test_simple_template_view(client):
    response = client.get("/simple", HTTP_HOST="example.com")
    assert response.status_code == 200
    assertInHTML(
        '<script defer data-domain="example.com" src="https://plausible.io/js/plausible.js"></script>',
        response.content.decode(),
    )


def test_custom_hostname(rf):
    request = rf.get("/", HTTP_HOST="example.com")
    rendered = _render_string(
        '{% load plausible %}{% plausible hostname="custom.com" %}',
        context=RequestContext(request),
    )
    assertInHTML(
        '<script defer data-domain="custom.com" src="https://plausible.io/js/plausible.js"></script>',
        rendered,
    )


def test_custom_domain(rf):
    request = rf.get("/")
    rendered = _render_string(
        '{% load plausible %}{% plausible plausible_domain="my-plausible.com" %}',
        context=RequestContext(request),
    )
    assertInHTML(
        '<script defer data-domain="testserver" src="https://my-plausible.com/js/plausible.js"></script>',
        rendered,
    )


def test_custom_script_name(rf):
    request = rf.get("/")
    rendered = _render_string(
        '{% load plausible %}{% plausible plausible_script_name="plausible.hash.js" %}',
        context=RequestContext(request),
    )
    assertInHTML(
        '<script defer data-domain="testserver" src="https://plausible.io/js/plausible.hash.js"></script>',
        rendered,
    )


def test_custom_domain_from_settings(settings, rf):
    settings.PLAUSIBLE_DOMAIN = "my-plausible.com"
    request = rf.get("/")
    rendered = _render_string(
        "{% load plausible %}{% plausible %}",
        context=RequestContext(request),
    )
    assertInHTML(
        '<script defer data-domain="testserver" src="https://my-plausible.com/js/plausible.js"></script>',
        rendered,
    )


def test_custom_script_name_from_settings(settings, rf):
    settings.PLAUSIBLE_SCRIPT_NAME = "plausible.hash.js"
    request = rf.get("/")
    rendered = _render_string(
        "{% load plausible %}{% plausible %}",
        context=RequestContext(request),
    )
    assertInHTML(
        '<script defer data-domain="testserver" src="https://plausible.io/js/plausible.hash.js"></script>',
        rendered,
    )
