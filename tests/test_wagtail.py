import pytest
from django.core.exceptions import ValidationError
from pytest_django.asserts import assertInHTML
from wagtail.core.models import Site

from plausible.contrib.wagtail.models import PlausibleSettings
from plausible.contrib.wagtail.validators import PlausibleScriptNameValidator


@pytest.fixture
def plausible_settings():
    return PlausibleSettings.for_site(Site.objects.get())


@pytest.mark.django_db
def test_simple_template_view(client):
    response = client.get("/simple-wagtail", HTTP_HOST="example.com")
    assert response.status_code == 200
    assertInHTML(
        '<script defer data-domain="example.com" src="https://plausible.io/js/plausible.js"></script>',
        response.content.decode(),
    )


@pytest.mark.django_db
def test_hostname_from_settings(client, plausible_settings):
    plausible_settings.site_domain = "from-settings.com"
    plausible_settings.save()
    response = client.get("/simple-wagtail")
    assert response.status_code == 200
    assertInHTML(
        '<script defer data-domain="from-settings.com" src="https://plausible.io/js/plausible.js"></script>',
        response.content.decode(),
    )


@pytest.mark.django_db
def test_script_name_from_settings(client, plausible_settings):
    plausible_settings.script_name = "plausible.hash.js"
    plausible_settings.save()
    response = client.get("/simple-wagtail")
    assert response.status_code == 200
    assertInHTML(
        '<script defer data-domain="testserver" src="https://plausible.io/js/plausible.hash.js"></script>',
        response.content.decode(),
    )


@pytest.mark.django_db
def test_plausible_domain_from_settings(client, plausible_settings):
    plausible_settings.plausible_domain = "my-plausible.com"
    plausible_settings.save()
    response = client.get("/simple-wagtail")
    assert response.status_code == 200
    assertInHTML(
        '<script defer data-domain="testserver" src="https://my-plausible.com/js/plausible.js"></script>',
        response.content.decode(),
    )


@pytest.mark.parametrize(
    "script_name", ["plausible.js", "plausible.hash.js", "plausible.hash.compat.js"]
)
def test_validates_script_name(script_name):
    PlausibleScriptNameValidator()(script_name)


@pytest.mark.parametrize(
    "script_name",
    [
        "left-pad.js",
        "plausible.io",
        "plausible..js",
        "plausible.nothing.js",
        "plausible.hash",
        "hash.js",
    ],
)
def test_invalid_script_names(script_name):
    with pytest.raises(ValidationError):
        PlausibleScriptNameValidator()(script_name)
