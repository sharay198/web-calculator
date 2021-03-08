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


# @pytest.mark.django_db
# def test_key_of_context_of_delete_page():
#     client = Client()
#     path = reverse('delete', kwargs={'id': 15})
#     print(path)
#     response = client.get(path)
#     assert 'expression' in response.context
#     # exp = Exp.expressions.get(id=5)
#     print(response.context)


def get_templates_name():
    path_to_templates = BASE_DIR + f'/calculator/templates/calculator/'
    list_of_templates = os.listdir(path_to_templates)
    list_of_templates.pop(2)  # remove base.html
    return list_of_templates  # ['expression_details.html', 'delete_expression.html', 'database.html', 'index.html']


@pytest.fixture(params=get_templates_name())
def template_name(request):
    # template = request.param
    path_to_template = BASE_DIR + f'/calculator/templates/calculator/{request.param}'
    content_of_template = open(path_to_template, 'r')
    return content_of_template


# def test_template_name(template_name):
#     print(template_name)


@pytest.fixture(params=[reverse('index'),
                        reverse('database'),
                        reverse('details', kwargs={'id': 100}),
                        reverse('delete', kwargs={'id': 35})])
def path(request):
    return request.param


# def test_path(path):
#     print(path)


@pytest.fixture()
def key_of_context(path):
    client = Client()
    response = client.get(path)
    key_of_context = response.context
    return key_of_context


# @pytest.mark.django_db
# def test_key_of_context(key_of_context):
#     print(key_of_context)


@pytest.mark.django_db
def test_equality_key_of_context_using_in_template_with_key_using_in_views(key_of_context, template_name):
    # path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template_name}.html'
    # assert
    # for template in get_templates_name():
    # content_of_template = open(template_name, 'r')
    print(key_of_context, template_name)
    # assert key_of_context in template_name


# @pytest.mark.parametrize('template_name, key_of_context',
#                          (('index', 'form'),
#                           ('database', 'expressions'),
#                           ('expression_details', 'expression'),
#                           ('delete_expression', 'expression')))
# def test_equality_key_of_context_using_in_template_with_key_using_in_views(template_name, key_of_context):
#     path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template_name}.html'
#     content_of_template = open(path_to_template, 'r')
#     assert key_of_context in content_of_template.read()

