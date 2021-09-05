from django.core.exceptions import ValidationError
from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PlausibleScriptNameValidator:
    """
    Validate a script name against allowed values


    See also https://plausible.io/docs/script-extensions
    """

    _regex = r"plausible([a-z.]*)\.js"
    valid_extensions = ["hash", "outbound-links", "exclusions", "compat", "local"]
    message = _("Enter a valid value.")

    def __init__(self):
        self.regex = _lazy_re_compile(self._regex)

    def __call__(self, value: str):
        regex_matches = self.regex.search(str(value))
        if regex_matches is None:
            raise ValidationError(self.message, code="invalid")

        extensions = regex_matches.group(1).split(".")

        try:
            extensions.remove("")
        except ValueError:
            pass

        for extension in extensions:
            if extension not in self.valid_extensions:
                raise ValidationError(self.message, code="invalid")
