from django.core.exceptions import ValidationError


def validate_result_of_exp(value):
    if value == ZeroDivisionError:
        raise ValidationError('You can not division by zero')
    return value
