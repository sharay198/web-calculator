from django.test import Client
from django.http import request
from calculator.forms import ExpForm
# from django.test import TestCase
from django.shortcuts import render
from calculator.views import get_exp
# Create your tests here.
c = Client()
file_index_html = open('index.html')
content = file_index_html.read()
key_in_template = content[182:187]


def test_key_of_context_in_get_exp():
    # bound_form = ExpForm(request.POST)
    # check whether it's valid:
    context = {'form': None}
    result = get_exp(request)
    assert (result == render(request, 'calculator/index.html', {'form': None}))
