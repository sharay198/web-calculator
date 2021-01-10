def check_remainder_of_result(value):
    """Return True if value is float and it's remainder equal zero False otherwise"""
    if isinstance(value, float) and value % 1 == 0:
        return True
    return False


def check_if_floordiv(expression):
    """Return True if expression has "//"  False otherwise"""
    if '//' in expression:
        return True
    return False


def calculate_expression(expression):
    """Return result of expression"""
    result_of_expression = eval(expression, {'__builtins__': {}})
    if check_remainder_of_result(result_of_expression):
        result_of_expression = int(result_of_expression)
    return result_of_expression
