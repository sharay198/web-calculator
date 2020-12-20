from django.core.exceptions import ValidationError

list_of_available_chars = '*/+-.0123456789)('


# remove to clean_result_of_exp of forms.py
def validate_result_of_exp(value):
    if value == ZeroDivisionError:
        raise ValidationError('You can not division by zero')
    return value


def check_string_s_action_floordiv(expression):
    if '//' in expression:
        return True
    return False


def check_expression(expression):
    try:
        eval(expression, {'__builtins__': {}})
    except ZeroDivisionError:
        raise ValidationError('You can not division on zero')
    except NameError:
        raise ValidationError('You have entered invalid data 1')
    except SyntaxError:
        raise ValidationError('You have entered invalid data 2')
    except KeyError:
        raise ValidationError('You have entered invalid data 3')
    except IndexError:
        raise ValidationError('You have entered invalid data 4')
    except TypeError:
        raise ValidationError('You have entered invalid data 5')
    else:
        if check_string_s_action_floordiv(expression) or not check_wrong_char_in_string(expression):
            raise ValidationError('Wrong data')
    #         raise ValidationError('Wrong data')
    return expression


def check(char):
    """if char in '*/+-.0123456789)(' return True otherwise False"""
    if char in list_of_available_chars:
        return True
    return False


def check_none_string(expression):
    if expression is None:
        raise ValidationError('You have entered wrong data 1')
    return expression


def check_empty_string(expression):
    if expression.isspace():
        return expression


def check_wrong_char_in_string(expression):
    for char in expression:
        if not check(char):
            return False
    return True


def check_string_s_action_exponentiation(expression):
    length = len(expression)
    for i in range(length):
        if expression[i] == '*':
            pass
            if expression[i + 1] != '*':
                raise ValidationError('Wrong action 1')
    return expression

# s = '1//'
# print(eval(s, {}))
# print(check_wrong_char_in_string('1-1'))
