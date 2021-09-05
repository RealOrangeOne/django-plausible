# django-plausible

![CI](https://github.com/RealOrangeOne/django-plausible/workflows/CI/badge.svg)
![PyPI](https://img.shields.io/pypi/v/django-plausible.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-plausible.svg)
![PyPI - Status](https://img.shields.io/pypi/status/django-plausible.svg)
![PyPI - License](https://img.shields.io/pypi/l/django-plausible.svg)


Django module to provide easy [Plausible](https://plausible.io/) integration, with [Wagtail](https://wagtail.io/) support.

## Installation

```
pip install django-plausible
```

Then simply add `plausible` to `INSTALLED_APPS`.

## Usage

`django-plausible` provides a `plausible` template tag, which can be used to output the required [script tag](https://plausible.io/docs/plausible-script) for Plausible.

```html
{% load plausible %}

{% plausible %}
```

Will result in:

```html
<script defer data-domain="example.com" src="https://plausible.io/js/plausible.js"></script>
```

### Configuration

Configuration can be changed either in `settings.py`, or when calling the `plausible` template tag:

- `PLAUSIBLE_DOMAIN`: The domain Plausible is running on (defaults to `plausible.io`)
- `PLAUSIBLE_SCRIPT_NAME`: The name of the script to use (defaults to `plausible.js`). See [script extensions](https://plausible.io/docs/script-extensions) for available options.

These settings will affect all calls to the `plausible` template tag. To override it at call time, you can also pass them into the template tag:

```
{% plausible plausible_domain="my-plausible.com" script_name="plausible.hash.js" %}
```

By default, the domain (`data-domain`) used will be based on the request's hostname (using [`request.get_host()`](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.get_host)). To override this, pass `site_domain` to the template tag.

If the ["compat" script](https://plausible.io/docs/script-extensions#plausiblecompatjs) is used, `django-plausible` will automatically add the required `id` to the `script` tag. It is excluded by default to help hide Plausible's presence.

## Usage with Wagtail

Additionally, `django-plausible` provides an (optional) deep integration with [Wagtail](https://wagtail.io), allowing configuration through the Wagtail admin. To enable this, additionally add `plausible.contrib.wagtail` to `INSTALLED_APPS`.

Configuration is done through the "Plausible Analytics" [setting](https://docs.wagtail.io/en/stable/reference/contrib/settings.html#settings):

- `site_domain`: the value for `data-domain`. If left blank (the default), the request's hostname will be used (as above), **not** the site hostname.
- `plausible_domain`: The domain Plausible is running on (as above)
- `script_name`: The name of the script to use (as above)

To access the template tag, load `plausible_wagtail`, rather than `plausible`. The template tag itself is still `plausible`. Note that unlike the Django variant, the Wagtail template tag doesn't allow options to be passed.

```html
{% load plausible_wagtail %}

{% plausible %}
```
