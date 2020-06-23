from datetime import datetime

from django.core.exceptions import ValidationError


def validate_str(value):
    if isinstance(value, str):
        print("{} is a string".format(value))
    else:
        raise ValidationError('%s is not a string' % value)


def validate_list(value):
    if isinstance(value, list):
        print("{} is a list".format(value))
    else:
        raise ValidationError('%s is not a list' % value)


def validate_int(value):
    if isinstance(value, int):
        print("{} is an integer".format(value))
    else:
        raise ValidationError("%s is not an integer" % value)


def validate_float(value):
    if isinstance(value, float):
        print("{} is a float".format(value))
    else:
        raise ValidationError("%s is not a float" % value)


def validate_dict(value):
    if isinstance(value, dict):
        print("{} is a dict".format(value))
    else:
        raise ValidationError("%s is not a dict" % value)


def validate_datetime(value, format):
    if isinstance(datetime.strptime(value, format), datetime):
        print("{} is a datetime".format(value))
    else:
        raise ValidationError("%s is not a datetime" % value)