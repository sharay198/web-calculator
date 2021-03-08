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


def get_templates_name():
    """Return list of templates, using in the application"""
    path_to_templates = BASE_DIR + f'/calculator/templates/calculator/'
    list_of_templates = os.listdir(path_to_templates)
    list_of_templates.pop(2)  # remove base.html
    return list_of_templates  # ['expression_details.html', 'delete_expression.html', 'database.html', 'index.html']


@pytest.fixture(params=get_templates_name())
def content_of_template(request):
    """Return content of template as string"""
    template = request.param
    path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template}'
    content_of_template = open(path_to_template, 'r').read()
    return content_of_template


def test_template_name(content_of_template):
    print(content_of_template)


@pytest.fixture(params=[reverse('details', kwargs={'id': 100}),
                        reverse('delete', kwargs={'id': 35}),
                        reverse('database'),
                        reverse('index')])
def path(request):
    return request.param


def test_path(path):
    print(path)


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


@pytest.mark.django_db
def test_key_of_context(key_of_context):
    print(key_of_context)


@pytest.mark.django_db
def test_equality_key_of_context_using_in_template_with_key_using_in_views(content_of_template, key_of_context):
    """Check if key of context in views.py equal key using in template"""
    if key_of_context in content_of_template:
        assert key_of_context in content_of_template
