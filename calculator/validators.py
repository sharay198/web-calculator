from django.core.exceptions import ValidationError
import os

# from settings import BASE_DIR
#
# list_of_available_chars = '*/+-.0123456789)('
#
# def get_templates_name():
#     path_to_templates = BASE_DIR + f'/calculator/templates/calculator/'
#     list_of_files = os.listdir(path_to_templates)
#     list_of_files.pop(2)
#     return list_of_files
# print(get_templates_name())





# remove to clean_result_of_exp of forms.py
def validate_result_of_exp(value):
    if isinstance(value, float) and value % 1 == 0:
        return True
    return False


def check_if_floordiv(expression):
    if '//' in expression:
        return True
    return False


def check_expression(expression):
    try:
        eval(expression, {'__builtins__': {}})
    except ZeroDivisionError:
        raise ValidationError('You can not division on zero')
    except (NameError, SyntaxError, KeyError, IndexError, TypeError):
        raise ValidationError('You have entered invalid data')
    else:
        if check_if_floordiv(expression) or not check_char_in_string(expression):
            raise ValidationError('You have entered invalid data 6')
    return expression


def check_char(char):
    """if char in '*/+-.0123456789)(' return True otherwise False"""
    if char in list_of_available_chars:
        return True
    return False


def check_char_in_string(expression):
    for char in expression:
        if not check_char(char):

            return False
    return True

