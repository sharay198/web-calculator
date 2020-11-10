import os
import sys

from django.conf import settings
from django.http import request
from django.urls import reverse, resolve
from django.test import RequestFactory
from django.shortcuts import render
# Create your tests here.
import pytest

#from calculator.forms import ExpForm
#from calculator.views import get_exp


# class TestVIews:
#
#     def test_views_get_exp_post(self):
#         d = {'exp': '1-1', 'result_of_exp': 0}
#         bound_form = ExpForm(d)
#         assert get_exp(request) == render(request, 'calculator/index.html', {'form': bound_form})

# def test_index_url(self):
#     path = reverse('index')
#     assert resolve(path).url_name == 'index'
#     print(path)
#     print(resolve(path).view_name)
#     print(resolve(path).func)


# class TestUrls:
settings.configure()

def test_index_url():
    path = reverse('index')
    # print(resolve(path).view_name)
    assert resolve(path).view_name == 'index'


# def test_exp_list_url():
#     path = reverse('database')
#     # print(resolve(path).view_name)
#     assert resolve(path).view_name == 'database'
