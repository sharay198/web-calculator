from django.core.exceptions import ValidationError

list_of_available_chars = '*/+-.0123456789)('


def validate_result_of_exp(value):
    if value == ZeroDivisionError:
        raise ValidationError('You can not division by zero')
    return value


def check(char):
    if char in list_of_available_chars:
        return True
    return False


def check_string(string):
    if string is None:
        raise ValidationError('You have entered wrong data 1')
    for char in string:
        if not check(char):
            raise ValidationError('You have entered wrong data in validator')
    return string


def check_empty_string(string):
    if string.isspace():
        return string


def check_string_s_action(string):
    length = len(string)
    if check_string(string):
        for i in range(length):
            if string[i] == '*' and string[i + 1] == '*':
                pass
            if string[i] == '/' and string[i + 1] == '/':
                # if string[i] == '/' and string[i + 1] != '(' or string[i + 1] not in '0123456789':
                raise ValidationError('Wrong action 1')
        return string

# s = 'a-(2-1)'
# print(eval(s, {}))
# print(check_string('1-(2-1)'))


# def calculate_exp(value):
#     if value
