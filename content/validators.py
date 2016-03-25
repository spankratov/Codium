from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError


class DefaultFromMinToMax(object):
    message = _('Default value for attribute must be between min_value and max_value.')

    def __init__(self, message=None):
        self.serializer_field = None
        self.message = message or self.message

    def set_context(self, serializer_field):
        instance = getattr(serializer_field.parent, 'instance', None)
        request = serializer_field.context['request']
        self.min_value = request.data.get('min_value', None) or getattr(instance, 'min_value', None)
        self.max_value = request.data.get('max_value', None) or getattr(instance, 'max_value', None)

    def __call__(self, value):
        if self.min_value is not None:
            if value < int(self.min_value):
                raise ValidationError(self.message)
        if self.max_value is not None:
            if value > int(self.max_value):
                raise ValidationError(self.message)


def from_zero_to_hundred(value):
    if value < 0 or value > 100:
        raise ValidationError('This field must be between 0 and 100.')
