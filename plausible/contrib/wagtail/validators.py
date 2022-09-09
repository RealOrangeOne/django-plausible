from os.path import basename

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from plausible.utils import is_valid_plausible_script


@deconstructible
class PlausibleScriptNameValidator:
    message = _("Enter a valid value (eg 'plausible.js').")

    def __call__(self, value: str):
        if basename(value) != value:
            raise ValidationError(self.message, code="invalid")

        if not is_valid_plausible_script(basename(value)):
            raise ValidationError(self.message, code="invalid")
