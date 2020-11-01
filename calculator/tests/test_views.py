from django.http import request
from django.urls import reverse, resolve
from django.test import RequestFactory
from django.shortcuts import render
# Create your tests here.
import pytest

from calculator.forms import ExpForm
from calculator.views import get_exp


def test_index():
    path = reverse('index')

    assert resolve(path).url_name == 'index'
    print(path)
    print(resolve(path).view_name)
    print(resolve(path).func)


def test_views_get_exp_post():
    d = {'exp': '1-1', 'result_of_exp': 0}
    bound_form = ExpForm(d)
    assert get_exp(request) == render(request, 'calculator/index.html', {'form': bound_form})

# @pytest.mark.django_db
# def test_get_exp():
#     d = {'exp': '(11+1*5)/4'}
#     bound_form = ExpForm(d)
#     path = reverse('index')
#     request = RequestFactory().post(path, data={'exp': '(11+1*5)/4'})
#     assert get_exp(request) == render(request, 'calculator/index.html', {'form': bound_form})
