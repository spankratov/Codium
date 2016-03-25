from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError, MethodNotAllowed
from userdata.models import Character


class LevelFromMinToMax(object):
    message = _('Value for attribute must be between min_value and max_value.')

    def __init__(self, message=None):
        self.serializer_field = None
        self.message = message or self.message

    def set_context(self, serializer_field):
        request = serializer_field.context['request']
        if request.method == 'POST':
            raise MethodNotAllowed('POST', 'AttributeLevels Serializer was launched in creation mode.')
        instance = serializer_field.parent.instance.attribute
        self.min_value = getattr(instance, 'min_value', None)
        self.max_value = getattr(instance, 'max_value', None)

    def __call__(self, value):
        if self.min_value is not None:
            if value < int(self.min_value):
                raise ValidationError(self.message)
        if self.max_value is not None:
            if value > int(self.max_value):
                raise ValidationError(self.message)


class NotBiggerThanCharacterDaysLived(object):
    message = _('Value for this field can not be bigger than days that character lived.')

    def __init__(self, message=None):
        self.serializer_field = None
        self.message = message or self.message

    def set_context(self, serializer_field):
        instance = getattr(serializer_field.parent, 'instance', None)
        request = serializer_field.context['request']
        if 'character_id' in request.data:
            self.days_lived = Character.objects.get(id=int(request.data['character_id'])).days_lived
        elif instance is not None:
            self.days_lived = instance.character.days_lived
        else:
            self.days_lived = 0

    def __call__(self, value):
        if value > self.days_lived:
            raise ValidationError(self.message)


def from_zero_to_hundred(value):
    if value < 0 or value > 100:
        raise ValidationError('This field must be between 0 and 100.')