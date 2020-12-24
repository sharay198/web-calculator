from django.shortcuts import render, redirect
from django.urls import reverse
from calculator.validators import validate_result_of_exp
from calculator.models import Exp
from calculator.forms import ExpForm


def check_remainder_of_value(value):
    """Return True if value is float and it's remainder equal zero value otherwise False"""
    return True if isinstance(value, float) and value % 1 == 0 else False


# Create your views here.
def calculate_expression(expression):
    """Calculate expression"""
    return eval(expression)


def make_dict_with_data_for_valid_form(expression):
    result_of_expression = eval(expression)
    if check_remainder_of_value(result_of_expression):
        result_of_expression = int(result_of_expression)
    return {'expression': expression, 'result_of_expression': result_of_expression}


def make_dict_with_data_for_form_with_error(expression):
    return {'expression': expression, 'result_of_expression': ''}


def get_expression(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bound_form = ExpForm(request.POST)
        # check whether it's valid:
        if bound_form.is_valid():
            print(request.POST)
            d = make_dict_with_data_for_valid_form(bound_form.cleaned_data['expression'])
            # expression = bound_form.cleaned_data['expression']
            # result = calculate_expression(expression)

            # d = {'expression': expression, 'result_of_expression': result}
            # if bound_form.has_changed():
            bound_form = ExpForm(d)
            bound_form.save()
            return render(request, 'calculator/index.html', context={'form': bound_form})
        elif bound_form.has_error('expression'):
            d = make_dict_with_data_for_form_with_error(request.POST['expression'])
            # d = {'expression': request.POST['expression'], 'result_of_expression': ''}
            bound_form = ExpForm(d)
            print(bound_form['expression'].errors)
            print(bound_form.errors)
            return render(request, 'calculator/index.html', context={'form': bound_form})
            # if bound_form.errors['expression']:
            #     unbound_form = ExpForm({})
            #     return render(request, 'calculator/index.html', context={'form': unbound_form})
    if request.method == 'GET':
        print(request.method)
        form = ExpForm()
        return render(request, 'calculator/index.html', context={'form': form})


def detail_of_expression(request, id):
    expression = Exp.expressions.get(id=id)
    return render(request, 'calculator/expression detail.html', context={'expression': expression})


def list_of_expressions(request):
    expressions = Exp.expressions.all()
    return render(request, 'calculator/database.html', context={'expressions': expressions})


def delete_expression(request, id):
    if request.method == 'GET':
        expression = Exp.expressions.get(id=id)
        print(reverse('delete', kwargs={'id': id}))
        return render(request, 'calculator/delete expression.html', context={'expression': expression})
    if request.method == 'POST':
        expression = Exp.expressions.get(id=id)
        expression.delete()
        return redirect(reverse('database'))




