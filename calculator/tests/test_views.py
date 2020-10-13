from django.urls import reverse
from django.test import RequestFactory
from django.shortcuts import render
# Create your tests here.
from calculator.views import get_exp


def test_get_exp():
    path = reverse('index')
    request = RequestFactory().post(path, data={'exp': '(11+1*5)/4'})

    assert get_exp(request) == render(request, 'calculator/index.html', {'exp': '(11+1*5)/4', 'result_of_exp': '4'})
