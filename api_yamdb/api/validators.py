import re

from rest_framework import serializers


def validate_username(value):
    if not re.match(r"^[a-zA-Z\d\@\.\+\-\_]*$", value):
        raise serializers.ValidationError('Поле username содержит '
                                          'запрещёные символы.')
    if value == 'me':
        raise serializers.ValidationError(
            'Нельзя использовать \'me\' в качестве юзернейма'
        )
    return value
