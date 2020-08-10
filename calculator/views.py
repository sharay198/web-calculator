from django.shortcuts import render
from calculator.models import Exp
from calculator.forms import ExpForm

# Create your views here.


def get_exp(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bound_form = ExpForm(request.POST)
        # check whether it's valid:
        if bound_form.is_valid():
            expression = bound_form.cleaned_data['exp']
            result = bound_form.cleaned_data['result_of_exp']
            d = {'exp': expression, 'result_of_exp': result}
            bound_form = ExpForm(d)
            bound_form.save()
            return render(request, 'calculator/index.html', {'bound_form': bound_form})
        else:
            d = {'exp': request.POST['exp'], 'result_of_exp': ''}
            bound_form = ExpForm(d)
            return render(request, 'calculator/index.html', {'bound_form': bound_form})
    if request.method == 'GET':
        form = ExpForm()
        return render(request, 'calculator/index.html', {'form': form})


def exp_list(request):
    exps = Exp.expressions.all()
    return render(request, 'calculator/database.html', context={'exps': exps})
