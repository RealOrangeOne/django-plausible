# django-plausible

![CI](https://github.com/RealOrangeOne/django-plausible/workflows/CI/badge.svg)
![PyPI](https://img.shields.io/pypi/v/django-plausible.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-plausible.svg)
![PyPI - Status](https://img.shields.io/pypi/status/django-plausible.svg)
![PyPI - License](https://img.shields.io/pypi/l/django-plausible.svg)


Django module to provide easy [Plausible](https://plausible.io/) integration, with Wagtail support.

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

These settings will affect all calls to the `plausible` template tag. To override it at call time, pass lowercased versions of these. eg:

```
{% plausible plausible_domain="my-plausible.com" %}
```

By default, the domain used will be based on the request's hostname (using [`request.get_host()`](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.get_host)). To override this, pass `hostname` to the template tag.

If the ["compat" script](https://plausible.io/docs/script-extensions#plausiblecompatjs) is used, `django-plausible` will automatically add the required `id` to the `script` tag. It is excluded by default to help hide Plausible's presence.
