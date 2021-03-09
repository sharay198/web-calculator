import pytest
from django.conf import settings
from django.test import Client
from web_calculator.settings import BASE_DIR, DATABASES
from calculator.views import *
import os


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}


@pytest.fixture(params=[reverse('details', kwargs={'id': 100}),  # /calculator/database/100/
                        reverse('delete', kwargs={'id': 35}),  # /calculator/database/35/delete/
                        reverse('database'),  # /calculator/database
                        reverse('index')])  # /calculator/
def path(request):
    return request.param


@pytest.fixture()
def key_of_context(path):
    client = Client()
    response = client.get(path)
    context_list = response.context
    _keys_of_context_using_in_views = ['expression', 'expression', 'expressions', 'form']
    keys = context_list.keys()
    for key in keys:
        if key in _keys_of_context_using_in_views:
            return key


@pytest.fixture()
def template(path):
    client = Client()
    response = client.get(path)
    template_using_in_views = response.templates
    for template in template_using_in_views:
        content_template_file = open(BASE_DIR + f'/calculator/templates/{template.name}', 'r').read()
        return content_template_file



@pytest.mark.django_db
def test_equality_key_of_context_using_in_template_with_key_using_in_views(template, key_of_context):
    """Check if key of context in views.py equal key using in template"""
    assert key_of_context in template
