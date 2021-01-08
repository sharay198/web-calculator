def check_remainder_of_result(value):
    if isinstance(value, float) and value % 1 == 0:
        value = int(value)
    return value


def calculate_expression(expression):
    result_of_expression = eval(expression, {'__buitins_': {}})
    return result_of_expression
